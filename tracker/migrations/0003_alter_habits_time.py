# Generated by Django 5.1.5 on 2025-02-01 23:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tracker", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habits",
            name="time",
            field=models.TimeField(
                default=datetime.time(23, 24, 12, 58910),
                verbose_name="Время выполнения",
            ),
        ),
    ]
