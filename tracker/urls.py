from django.urls import path
from tracker.apps import TrackerConfig
from .views import (
    HabitsListApiView,
    HabitsCreateApiView,
    HabitsRetrieveApiView,
    HabitsUpdateApiView,
    HabitsDestroyApiView,
)


app_name = TrackerConfig.name

urlpatterns = [
    path("habits/", HabitsListApiView.as_view(), name="habits_list"),
    path("habits/create/", HabitsCreateApiView.as_view(), name="habits_create"),
    path("habits/<int:pk>/", HabitsRetrieveApiView.as_view(), name="habits_retrieve"),
    path(
        "habits/<int:pk>/update/", HabitsUpdateApiView.as_view(), name="habits_update"
    ),
    path(
        "habits/<int:pk>/delete/", HabitsDestroyApiView.as_view(), name="habits_delete"
    ),
]
