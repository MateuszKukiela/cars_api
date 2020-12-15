# Generated by Django 3.1.4 on 2020-12-15 15:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rate",
            name="car",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="rates",
                to="api.car",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="car",
            unique_together={("make", "model")},
        ),
    ]