from datetime import timedelta

from rest_framework import serializers


class HabitValidator:
    """Валидатор привычек."""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value["time_to_action"] > timedelta(seconds=120):
            raise serializers.ValidationError(
                "Время выполнения привычки не может превышать 120 секунд."
            )

        if value["period"] > 7:
            raise serializers.ValidationError(
                "Периодичность выполнения привычки не может быть реже раза в неделю."
            )

        if value["connection_wont"] and value["reward"]:
            raise serializers.ValidationError(
                "Нельзя выбирать связанную привычку и вознаграждение одновременно."
            )

        if value["is_pleasant"]:
            if value["reward"] or value["connection_wont"]:
                raise serializers.ValidationError(
                    "Нельзя выбирать связанную привычку или вознаграждение для приятной привычки."
                )

        if value["connection_wont"]:
            if not value["connection_wont"].is_pleasant:
                raise serializers.ValidationError(
                    "В связанные привычки можно выбрать только привычки с признаком приятной привычки."
                )
