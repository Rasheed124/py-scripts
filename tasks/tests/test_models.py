from django.contrib.auth import get_user_model
from django.test import TestCase

from tasks.models import Task


User = get_user_model()


class TaskModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="modeluser",
            password="TestPassword123!",
        )

    def test_task_creation(self):
        task = Task.objects.create(
            user=self.user,
            title="Learn Django Testing",
            priority=Task.Priority.HIGH,
        )

        self.assertEqual(task.title, "Learn Django Testing")
        self.assertEqual(task.priority, Task.Priority.HIGH)
        self.assertFalse(task.completed)

    def test_task_string_representation(self):
        task = Task.objects.create(
            user=self.user,
            title="Build Todo Application",
        )

        self.assertEqual(str(task), "Build Todo Application")

    def test_task_default_priority(self):
        task = Task.objects.create(
            user=self.user,
            title="Understand Django Models",
        )

        self.assertEqual(task.priority, Task.Priority.MEDIUM)
