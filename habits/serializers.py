from rest_framework import serializers

from habits.models import Habits


class HabitSerializer(serializers.Serializer):
    class Meta:
        model = Habits
        fields = "__all__"
