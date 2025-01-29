from django.contrib import admin

from .models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "place",
        "time",
        "action",
        "is_pleasant",
        "connection_wont",
        "period",
        "reward",
        "time_to_action",
        "is_published",
    )
    search_fields = ["action", "time", "place"]
    list_filter = ["user", "is_pleasant", "is_published"]
