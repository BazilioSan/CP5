from django.utils import timezone
from rest_framework.generics import (CreateAPIView, DestroyAPIView,
                                     ListAPIView, RetrieveAPIView,
                                     UpdateAPIView)
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsCreator

from .models import Habits
from .pagination import PageSize
from .serializers import HabitsSerializer


class HabitsPublicListApiView(ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = PageSize

    def get_queryset(self):
        return Habits.objects.filter(is_published=True)


class HabitsUsersListApiView(ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    pagination_class = PageSize

    def get_queryset(self):
        return Habits.objects.filter(user=self.request.user)


class HabitsCreateApiView(CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def perform_create(self, serializer):
        habit = serializer.save(
            user=self.request.user, last_action_date=timezone.now().date()
        )
        habit.save()


class HabitsRetrieveApiView(RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsCreator]



class HabitsUpdateApiView(UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsCreator]


class HabitsDestroyApiView(DestroyAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

    def get_permissions(self):
        self.permission_classes = (IsCreator,)
        return super().get_permissions()
