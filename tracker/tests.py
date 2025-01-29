from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from tracker.models import Habits

class HabitsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.test_habit = Habits.objects.create(
        user=self.user,
        place="Test",
        action="Test",
        is_pleasant=True,
        time_to_action=100,
        period=5,
        is_published=True)
        self.client.force_authenticate(user=self.user)
    def test_habit_retrieve(self):
        url = reverse("tracker:habits_retrieve", args=(self.test_habit.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("action")
        self.assertEqual(result, self.test_habit.action_to_do)
    def test_habit_create(self):
        url = reverse("tracker:habits_create")
        data = {"place": "Test", "action": "Test", "is_pleasant": False, "period": 5, "time_to_do": 100, "is_published": True, "connection_wont": self.test_habit.id, 'reward': ""}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habits.objects.all().count(), 2)
    def test_habit_update(self):
        url = reverse("tracker:habits_update", args=(self.test_habit.id,))
        data = {"place_to_do": "Test_new", "action_to_do": "Test_new", "is_pleasant": True, "periodicity": 2, "duration": 100, "is_public": True, "related_habit": "", 'reward': ""}
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        result = response.json().get("place_to_do")
        self.assertEqual(result, data.get("place_to_do"))
    def test_habit_delete(self):
        url = reverse("tracker:habits_delete", args=(self.test_habit.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habits.objects.all().count(), 0)
