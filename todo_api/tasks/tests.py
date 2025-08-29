from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from tasks.models import Task

class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="john", password="1234")
        self.client.login(username="john", password="1234")

        
        self.signup_url = reverse("signup")       # /api/signup/
        self.login_url = reverse("login")         # /api/login/
        self.logout_url = reverse("logout")       # /api/logout/
        self.tasks_url = reverse("task-list")     # /api/tasks/
        

        # Create sample task
        self.task = Task.objects.create(
            owner=self.user,
            title="Sample Task",
            description="Test desc",
            category="work",
            due_date="2025-09-01",
            priority="important"
        )

    def test_user_signup(self):
        data = {"username": "newuser", "password": "test123"}
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login_and_logout(self):
        # Login
        response = self.client.post(self.login_url, {"username": "john", "password": "1234"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Logout
        response = self.client.post(self.logout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_tasks(self):
        response = self.client.get(self.tasks_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_task(self):
        data = {
            "title": "New Task",
            "description": "Testing create",
            "category": "personal",
            "due_date": "2025-09-05",
            "priority": "normal"
        }
        response = self.client.post(self.tasks_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_task(self):
        url = reverse("task-detail", args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Sample Task")

    def test_update_task_put(self):
        url = reverse("task-detail", args=[self.task.id])
        data = {
            "title": "Updated Task",
            "description": "Updated desc",
            "category": "work",
            "due_date": "2025-09-02",
            "priority": "normal",
            "completed": True
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Task")

    def test_partial_update_task_patch(self):
        url = reverse("task-detail", args=[self.task.id])
        data = {"completed": True}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["completed"])

    def test_delete_task(self):
        url = reverse("task-detail", args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_tasks_by_priority(self):
        response = self.client.get(self.tasks_url + "?priority=important")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for task in response.data:
            self.assertEqual(task["priority"], "important")

    def test_filter_tasks_by_category(self):
        response = self.client.get(self.tasks_url + "?category=work")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for task in response.data:
            self.assertEqual(task["category"], "work")
