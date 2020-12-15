# Generated by Django 3.1.4 on 2020-12-14 15:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "make",
                    models.CharField(
                        help_text="Car make. Max 255 characters", max_length=255
                    ),
                ),
                (
                    "model",
                    models.CharField(
                        help_text="Car model. Max 255 characters", max_length=255
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "rating",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ]
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.car"
                    ),
                ),
            ],
        ),
    ]
