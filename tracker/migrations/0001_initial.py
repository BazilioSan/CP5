# Generated by Django 5.1.5 on 2025-01-29 09:19

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habits",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("place", models.CharField(max_length=100, verbose_name="Место")),
                (
                    "time",
                    models.TimeField(
                        default=datetime.datetime(
                            2025, 1, 29, 9, 19, 50, 555696, tzinfo=datetime.timezone.utc
                        ),
                        verbose_name="Время выполнения",
                    ),
                ),
                ("action", models.CharField(max_length=100, verbose_name="Действие")),
                (
                    "is_pleasant",
                    models.BooleanField(
                        default=True, verbose_name="Признак приятной привычки"
                    ),
                ),
                ("period", models.PositiveIntegerField()),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name="Вознаграждение",
                    ),
                ),
                (
                    "time_to_action",
                    models.DurationField(
                        default=datetime.timedelta(seconds=60),
                        verbose_name="Время на выполнения",
                    ),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        default=True, verbose_name="Признак публичности"
                    ),
                ),
                (
                    "connection_wont",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="tracker.habits",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]
