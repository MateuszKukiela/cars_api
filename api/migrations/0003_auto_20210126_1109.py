# Generated by Django 3.1.4 on 2021-01-26 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201215_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rate',
            old_name='car',
            new_name='car_id',
        ),
    ]
