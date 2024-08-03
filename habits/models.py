from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="User", help_text="Habit owner")
    place = models.CharField(max_length=50, verbose_name="Place", help_text="Habit place")
    time = models.TimeField(verbose_name="Time", help_text="Habit time")
    action = models.CharField(max_length=50, verbose_name="Action", help_text="Habit action")
    is_pleasant = models.BooleanField(default=False, verbose_name="Pleasant", help_text="Is habit pleasant?")
    related_to = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Related habit", help_text="Related to", **NULLABLE)
    periodicity = models.PositiveSmallIntegerField(default=1, verbose_name="Periodicity", help_text="Edit habit periodicity in days")
    award = models.CharField(max_length=50, verbose_name="Award", help_text="Edit award for doing habit")
    execution_time = models.PositiveSmallIntegerField(default=120, verbose_name="Execution time", help_text="Edit habit execution time in seconds")
    is_public = models.BooleanField(default=False, verbose_name="Public", help_text="Is habit for public view?")

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Habit"
        verbose_name_plural = "Habits"
