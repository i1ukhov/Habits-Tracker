from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginators import CustomPagination
from habits.serializers import HabitSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitsListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    pagination_class = CustomPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        q = self.queryset.filter(user=self.request.user)
        return q


class HabitsRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


class HabitsDestroyAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habits.objects.all()
    permission_classes = (IsAuthenticated, IsOwner)


# Контроллер для просмотра списка публичных привычек
