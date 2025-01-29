from rest_framework.serializers import ModelSerializer
from .models import Habits


class HabitsSerializer(ModelSerializer):
    class Meta:
        model = Habits
        fields = "__all__"
