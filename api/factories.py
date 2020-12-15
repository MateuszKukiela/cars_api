from random import randint

import factory
from faker import Factory

from api.constants import MAX_RATING, MIN_RATING
from api.models import Car, Rate

faker = Factory.create()


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car

    make = factory.Sequence(lambda n: "make_%d" % n)
    model = factory.Sequence(lambda n: "model_%d" % n)


class RateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Rate

    car = factory.SubFactory(CarFactory)
    rating = randint(MIN_RATING, MAX_RATING)
