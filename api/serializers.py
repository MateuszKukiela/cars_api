from rest_framework import serializers

from api.constants import (
    CAR_MAKE_MAX_LENGTH,
    CAR_MODEL_MAX_LENGTH,
    MAX_RATING,
    MIN_RATING,
)
from api.models import Car, Rate


class CarSerializer(serializers.HyperlinkedModelSerializer):
    make = serializers.CharField(
        max_length=CAR_MAKE_MAX_LENGTH, help_text="Car make. Max 255 characters."
    )
    model = serializers.CharField(
        max_length=CAR_MODEL_MAX_LENGTH, help_text="Car model. Max 255 characters."
    )
    avg_rating = serializers.SerializerMethodField()
    rates_number = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ("id", "make", "model", "avg_rating", "rates_number")

    def get_avg_rating(self, obj):
        try:
            return obj.avg_rating
        except AttributeError:
            return None

    def get_rates_number(self, obj):
        try:
            return obj.rates_number
        except AttributeError:
            return None


class RateSerializer(serializers.HyperlinkedModelSerializer):
    car = serializers.PrimaryKeyRelatedField(
        queryset=Car.objects.all(), help_text="ID of car to rate."
    )
    rating = serializers.IntegerField(
        min_value=MIN_RATING,
        max_value=MAX_RATING,
        help_text="Rating as an integer from 1 to 5.",
    )

    class Meta:
        model = Rate
        fields = ("id", "car", "rating")
