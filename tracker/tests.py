from datetime import timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from tracker.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self):
        """Подготовка исходных данных для тестирования."""
        self.user = User.objects.create(email="test@test.com")
        self.test_habit = Habits.objects.create(
            user=self.user,
            place="Test",
            action="Test",
            is_pleasant=True,
            period=100,
            time_to_action=timedelta(seconds=300),
            is_published=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тестирование получения информации о привычке."""
        url = reverse("tracker:habits_retrieve", args=(self.test_habit.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("action")
        self.assertEqual(result, self.test_habit.action)

    def test_habit_create(self):
        """Тестирование создания новой привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "is_pleasant": False,
            "period": 5,
            "time_to_action": str(timedelta(seconds=300)),
            "is_published": True,
            "connection_wont": self.test_habit.id,
            "reward": "",
        }
        # response = self.client.post(url, data=data)
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Habits.objects.all().count(), 2)
        response = self.client.post(
            url, data=data, format="json"
        )  # Укажите формат JSON
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            Habits.objects.all().count(), 2
        )  # Убедитесь, что объект создан

        # Проверяем, что данные в базе соответствуют отправленным
        new_habit = Habits.objects.latest("id")
        self.assertEqual(new_habit.place, data["place"])
        self.assertEqual(new_habit.action, data["action"])

    def test_habit_update(self):
        """Тестирование изменения привычки."""
        url = reverse("tracker:habits_update", args=(self.test_habit.id,))
        data = {
            "place": "Test_new",
            "action": "Test_new",
            "is_pleasant": True,
            "period": 2,
            "time_to_action": str(timedelta(seconds=300)),
            "is_published": True,
            "connection_wont": "",
            "reward": "",
        }
        # response = self.client.patch(url, data=data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
        # result = response.json().get("place")
        # self.assertEqual(result, data.get("place"))
        response = self.client.patch(url, data=data, format="json")
        if response.status_code != status.HTTP_200_OK:
            print(response.json())  # Вывод ошибок для диагностики
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Проверяем, что данные успешно обновлены
        updated_habit = Habits.objects.get(id=self.test_habit.id)
        self.assertEqual(updated_habit.place, data["place"])
        self.assertEqual(updated_habit.action, data["action"])

    def test_habit_delete(self):
        """Тестирование удаления привычки."""
        url = reverse("tracker:habits_delete", args=(self.test_habit.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)

    def test_habit_list_public(self):
        """Тестирование получения списка публичных привычек."""
        url = reverse("tracker:public_habits_list")
        response = self.client.get(url)

        # готовим данные для сравнения - id привычки, признак публичности привычки и id создателя привычки
        result = {
            "id": self.test_habit.id,
            "is_published": self.test_habit.is_published,
            "user": self.user.id,
        }

        # выбираем из response данные для сравнения - d привычки, признак публичности привычки и id создателя привычки
        habit_id = response.json().get("results")[0].get("id")
        user_id = response.json().get("results")[0].get("user").get("id")
        is_published = response.json().get("results")[0].get("is_published")
        result_to_assert = {
            "id": habit_id,
            "is_published": is_published,
            "user": user_id,
        }

        # сравнение кодов ответа с ожидаемыми данными и подготовленных данных с выбранными
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result_to_assert, result)

    def test_habit_list_users(self):
        """Тестирование получения списка пользовательских привычек."""
        url = reverse("tracker:users_habits_list")
        response = self.client.get(url)

        # готовим данные для сравнения - id привычки, действие привычки и id создателя привычки
        result = {
            "id": self.test_habit.id,
            "action": self.test_habit.action,
            "user": self.user.id,
        }

        # выбираем из response данные для сравнения - id привычки, действие привычки и id создателя привычки
        habit_id = response.json().get("results")[0].get("id")
        action = response.json().get("results")[0].get("action")
        user_id = response.json().get("results")[0].get("user").get("id")
        result_to_assert = {
            "id": habit_id,
            "action": action,
            "user": user_id,
        }

        # сравнение кодов ответа с ожидаемыми данными и подготовленных данных с выбранными
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result_to_assert, result)

    def test_habit_create_wrong_duration(self):
        """Тестирование получения сообщения о неверной длительности при создании привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "is_pleasant": False,
            "period": 5,
            "time_to_action": str(timedelta(seconds=3000)),
            "is_published": True,
            "connection_wont": self.test_habit.id,
            "reward": "",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Время выполнения привычки не может превышать 120 секунд."],
        )

    def test_habit_create_wrong_periodicity(self):
        """Тестирование получения сообщения о неверной периодичности при создании привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "is_pleasant": False,
            "period": 10,
            "time_to_action": str(timedelta(seconds=120)),
            "is_published": True,
            "connection_wont": self.test_habit.id,
            "reward": "",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Периодичность выполнения привычки не может быть реже раза в неделю."],
        )

    def test_habit_create_reward_related_habit(self):
        """Тестирование получения сообщения об одновременно выборе награды
        и связанной привычки при создании привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "is_pleasant": False,
            "period": 2,
            "time_to_action": str(timedelta(seconds=120)),
            "is_published": True,
            "connection_wont": self.test_habit.id,
            "reward": "Test",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            ["Нельзя выбирать связанную привычку и вознаграждение одновременно."],
        )

    def test_habit_create_reward_for_pleasant_habit(self):
        """Тестирование получения сообщения о неверном выборе награды
        и связанной привычки при создании приятной привычки."""
        url = reverse("tracker:habits_create")
        data = {
            "place": "Test",
            "action": "Test",
            "is_pleasant": True,
            "period": 2,
            "time_to_action": str(timedelta(seconds=120)),
            "is_published": True,
            "connection_wont": "",
            "reward": "Test",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json().get("non_field_errors"),
            [
                "Нельзя выбирать связанную привычку или вознаграждение для приятной привычки."
            ],
        )
