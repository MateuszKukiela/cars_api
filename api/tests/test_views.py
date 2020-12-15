from unittest.mock import patch

from django.db.models import Count
from rest_framework import status
from rest_framework.test import APITestCase

from api.factories import CarFactory, RateFactory
from api.models import Car, Rate


class TestApi(APITestCase):
    def setUp(self):
        self.test_car = CarFactory(make="Volkswagen", model="Golf")
        self.ratings = RateFactory(car=self.test_car)
        self.test_cars = CarFactory.create_batch(4)

    def test_get_cars(self):
        # Boris wants to checkout what car are in the database
        response = self.client.get("/cars/", format="json")
        response_content = response.json()
        assert len(response_content) == Car.objects.count()

    @patch("api.views.requests.get")
    def test_post_car_wrong_make(self, mock_get):
        # Content with the database he wants to add a car
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"Results": []}
        response = self.client.post(
            "/cars/", {"make": "Wolkswagen", "model": "Impreza"}
        )
        # But he misspelled Volkswagen
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("api.views.requests.get")
    def test_post_car_wrong_model(self, mock_get):
        # He corrected himself
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"Results": [{"Model_Name": "Golf"}]}
        response = self.client.post(
            "/cars/", {"make": "Volkswagen", "model": "Impreza"}
        )
        # But Volkswagen doesn't make Impreza
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("api.views.requests.get")
    def test_post_vpic_error(self, mock_get):
        # Now he made no errors but vpic API is unavailable
        mock_get.return_value.status_code = 400
        response = self.client.post("/cars/", {"make": "Volkswagen", "model": "Golf"})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("api.views.requests.get")
    def test_post_car_already_exists(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"Results": [{"Model_Name": "Golf"}]}
        response = self.client.post("/cars/", {"make": "Volkswagen", "model": "Golf"})
        # Boris didn't notice Golf is already in the database
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @patch("api.views.requests.get")
    def test_post_car(self, mock_get):
        # Ho inputs his second favourite car
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "Results": [{"Model_Name": "Passat"}]
        }
        response = self.client.post("/cars/", {"make": "Volkswagen", "model": "Passat"})
        # Finally everything is good
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_rate_car_to_big(self):
        # Now Boris wants to rate his car
        # It is the bestest car so he gives it 10 points
        response = self.client.post("/rate/", {"car": self.test_car.id, "rating": 10})
        # But 10 is too much
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rate_car_to_small(self):
        # Angry Boris tries 0
        # test_car = CarFactory(make='Volkswagen', model='Golf')
        response = self.client.post("/rate/", {"car": self.test_car.id, "rating": 0})
        # But 0 is too small
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rate_car(self):
        # After reading docs he rates his car 5
        # test_car = CarFactory(make='Volkswagen', model='Golf')
        response = self.client.post("/rate/", {"car": self.test_car.id, "rating": 5})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_popular(self):
        # Now boris checks what car is most popular
        RateFactory.create_batch(5, car=self.test_car)
        response = self.client.get("/popular/")
        most_popular = (
            Rate.objects.annotate(car_object=Count("car"))
            .order_by("-car_object")[0]
            .car
        )
        assert response.json()[0]["id"] == most_popular.id
