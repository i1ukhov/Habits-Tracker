from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = ("pk", "action", "place", "time", "execution_time")
    search_fields = ("pk", "action", "place", "time")
    list_filter = ("id", "action", "place", "time")
