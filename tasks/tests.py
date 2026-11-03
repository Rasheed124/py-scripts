
from django.test import TestCase

from .models import Task
from django.urls import reverse

from datetime import timedelta

from django.utils import timezone

from .models import Task


class TaskModelTests(TestCase):

    def test_task_creation(self):
        task = Task.objects.create(
            title="Learn Django Testing",
            priority=Task.Priority.HIGH,
        )

        self.assertEqual(task.title, "Learn Django Testing")
        self.assertEqual(task.priority, Task.Priority.HIGH)
        self.assertFalse(task.completed)

    def test_task_string_representation(self):
        task = Task.objects.create(
            title="Build Todo Application",
        )

        self.assertEqual(str(task), "Build Todo Application")

    def test_task_default_priority(self):
        task = Task.objects.create(
            title="Understand Django Models",
        )

        self.assertEqual(task.priority, Task.Priority.MEDIUM)



class TaskCreateViewTests(TestCase):

    def test_create_task_page_returns_200(self):
        response = self.client.get(reverse("tasks:create"))

        self.assertEqual(response.status_code, 200)

    def test_create_task_successfully(self):
        response = self.client.post(
            reverse("tasks:create"),
            {
                "title": "Build Todo Application",
                "description": "Implement Django CRUD.",
                "priority": Task.Priority.HIGH,
                "due_date": "",
            },
        )

        self.assertEqual(Task.objects.count(), 1)

        task = Task.objects.get()

        self.assertEqual(task.title, "Build Todo Application")
        self.assertEqual(task.priority, Task.Priority.HIGH)

        self.assertRedirects(response, reverse("tasks:list"))

    def test_create_task_with_empty_title(self):
        response = self.client.post(
            reverse("tasks:create"),
            {
                "title": "",
                "description": "A task without a title.",
                "priority": Task.Priority.MEDIUM,
                "due_date": "",
            },
        )

        self.assertEqual(Task.objects.count(), 0)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context["form"],
            "title",
            "This field is required.",
        )







class TaskListFeatureTests(TestCase):

    def setUp(self):
        today = timezone.localdate()

        self.task_one = Task.objects.create(
            title="Learn Django",
            description="Study Django ORM",
            priority="high",
            completed=False,
            due_date=today,
        )

        self.task_two = Task.objects.create(
            title="Build Portfolio",
            description="Create a developer portfolio",
            priority="medium",
            completed=True,
            due_date=today + timedelta(days=3),
        )

        self.task_three = Task.objects.create(
            title="Read Python",
            description="Practice Python fundamentals",
            priority="low",
            completed=False,
            due_date=today - timedelta(days=2),
        )

    def test_search_by_title(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"q": "Django"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django")
        self.assertNotContains(response, "Build Portfolio")

    def test_search_by_description(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"q": "developer portfolio"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Build Portfolio")

    def test_completed_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"status": "completed"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Build Portfolio")
        self.assertNotContains(response, "Learn Django")

    def test_pending_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"status": "pending"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django")
        self.assertNotContains(response, "Build Portfolio")

    def test_priority_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"priority": "high"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django")
        self.assertNotContains(response, "Read Python")

    def test_overdue_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"schedule": "overdue"}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Read Python")
        self.assertNotContains(response, "Build Portfolio")




