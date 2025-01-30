from django.contrib import admin

from .models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "creator",
        "place",
        "time",
        "action",
        "is_pleasant",
        "connection_wont",
        "period",
        "reward",
        "time_to_action",
        "is_published",
        "last_action_date",
    )
    search_fields = ["action", "time", "place"]
    list_filter = ["creator", "is_pleasant", "is_published"]
