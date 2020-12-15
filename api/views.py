import requests
from django.db.models import Avg, Count
from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from api.constants import TOP_POPULAR
from api.models import Car, Rate
from api.serializers import CarSerializer, RateSerializer


class CarViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    """
    list:
    Return all cars in database.

    create:
    Create a new car instance.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = None
    http_method_names = ["get", "post"]

    def get_queryset(self):
        return self.queryset.annotate(avg_rating=Avg("rates__rating")).order_by("id")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{data["make"]}?format=json'
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()["Results"]
            models = [d["Model_Name"] for d in response_data]
            if data["model"] in models:
                self.perform_create(serializer)
            else:
                return Response(
                    {"error": "Car make or model does not exist"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        else:
            return Response({"error": "Connection failed"}, status=response.status_code)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class RateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    create:
    Create a new rate instance.
    """
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    http_method_names = ["post"]


class PopularViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list:
    Return top cars by number of rates in database.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = None
    http_method_names = ["get"]

    def get_queryset(self):
        self.queryset = self.queryset.annotate(avg_rating=Avg("rates__rating"))
        self.queryset = self.queryset.annotate(
            rates_number=Count("rates__rating")
        ).order_by("-rates_number")
        return self.queryset[:TOP_POPULAR]