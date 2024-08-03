from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitTestCase(APITestCase):
    """Тесты модели Habits."""

    def setUp(self):
        self.user = User.objects.create(email="test@test.test", password="test")
        self.client.force_authenticate(user=self.user)
        self.habit = Habits.objects.create(
            user=self.user,
            place="дом",
            time="23:00:00",
            action="спать",
        )

    def test_create_habit(self):
        """Тестирование создания привычки."""
        url = reverse("habits:habits_create")
        data = {
            "user": self.user.pk,
            "place": "улица",
            "time": "08:30:00",
            "action": "бегать",
        }
        response = self.client.post(url, data=data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data.get("user"), self.user.pk)
        self.assertEqual(data.get("place"), "улица")
        self.assertEqual(data.get("time"), "08:30:00")
        self.assertEqual(data.get("action"), "бегать")
        self.assertEqual(data.get("execution_time"), 120)

    def test_list_habit(self):
        """Тестирование вывода списка привычек."""
        response = self.client.get(reverse("habits:habits_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        """Тестирование просмотра одной привычки."""
        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("user"), self.habit.user.id)
        self.assertEqual(data.get("place"), self.habit.place)
        self.assertEqual(data.get("time"), self.habit.time)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_update_habit(self):
        """Тестирование изменения привычки."""
        url = reverse("habits:habits_update", args=(self.habit.pk,))
        data = {
            "user": self.user.pk,
            "place": "Парк",
            "time": "09:00:00",
            "action": "бег в парке",
        }
        response = self.client.put(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("user"), self.habit.user.id)
        self.assertEqual(data.get("place"), "Парк")
        self.assertEqual(data.get("time"), "09:00:00")
        self.assertEqual(data.get("action"), "бег в парке")

    def test_delete_habit(self):
        """Тестирование удаления привычки."""
        url = reverse("habits:habits_delete", args=(self.habit.pk,))
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_public_habit(self):
        """Тестирование вывода публичных привычек."""
        response = self.client.get(reverse("habits:public_habits_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
