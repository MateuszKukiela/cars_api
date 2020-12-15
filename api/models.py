from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from api.constants import (
    CAR_MAKE_MAX_LENGTH,
    CAR_MODEL_MAX_LENGTH,
    MAX_RATING,
    MIN_RATING,
)


class Car(models.Model):
    make = models.CharField(
        max_length=CAR_MAKE_MAX_LENGTH,
        blank=False,
        help_text="Car make. Max 255 characters",
    )
    model = models.CharField(
        max_length=CAR_MODEL_MAX_LENGTH,
        blank=False,
        help_text="Car model. Max 255 characters",
    )

    class Meta:
        unique_together = (
            "make",
            "model",
        )

    def __str__(self):
        return f"{self.make} {self.model}"


class Rate(models.Model):
    car = models.ForeignKey(Car, related_name="rates", on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(MIN_RATING), MaxValueValidator(MAX_RATING)],
        blank=False,
    )
