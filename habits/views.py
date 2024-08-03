from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

from habits.models import Habits
from habits.serializers import HabitSerializer


class HabitsCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    # добавить метод perform_create с установлением владельца


class HabitsListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    # поставить не all, а filter на владельца


class HabitsRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()


class HabitsUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()


class HabitsDestroyAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
