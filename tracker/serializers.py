from rest_framework.serializers import ModelSerializer
from .models import Habits
from .validators import HabitValidator
from .validators import action_time, action_periodicity


class HabitsSerializer(ModelSerializer):

    creator = UserSerializer(read_only=True)

    class Meta:
        model = Habits
        fields = "__all__"
