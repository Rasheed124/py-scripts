
from django.test import TestCase

from .models import Task
from django.urls import reverse


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







