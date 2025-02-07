from django.db import models
from django.utils import timezone

from tracker.constants import NULLABLE
from users.models import User


class Habits(models.Model):

    CHOICES_PERIOD = (
        ("daily", "Ежедневная"),
        ("weekly", "Еженедельная"),
        ("monthly", "Ежемесячная"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, **NULLABLE, verbose_name="Создатель"
    )
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(
        default=timezone.now().time(), verbose_name="Время выполнения"
    )
    action = models.CharField(max_length=100, verbose_name="Действие")
    is_pleasant = models.BooleanField(
        default=True, verbose_name="Признак приятной привычки"
    )
    connection_wont = models.ForeignKey(
        "self", on_delete=models.SET_NULL, **NULLABLE, verbose_name="Связанная привычка"
    )
    period = models.PositiveIntegerField()
    reward = models.CharField(max_length=100, **NULLABLE, verbose_name="Вознаграждение")
    # time_to_action = models.PositiveIntegerField(
    #     default=60, verbose_name="Время на выполнения"
    time_to_action = models.DurationField(
        default=timezone.timedelta(seconds=60), verbose_name="Время на выполнение"
    )
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")
    last_action_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего выполнения привычки",
        help_text="Введите дату последнего выполнения привычки",
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"
