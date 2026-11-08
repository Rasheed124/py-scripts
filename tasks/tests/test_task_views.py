from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


User = get_user_model()


class TaskCreateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="creator",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

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
        self.assertEqual(task.user, self.user)

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



class TaskDetailViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="detailuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.task = Task.objects.create(
            user=self.user,
            title="Learn Django Testing",
            description="Understand Django test cases.",
            priority=Task.Priority.HIGH,
        )

    def test_user_can_view_task_detail(self):
        response = self.client.get(
            reverse(
                "tasks:detail",
                kwargs={"task_id": self.task.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Learn Django Testing")


class TaskUpdateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="updateuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.task = Task.objects.create(
            user=self.user,
            title="Old Task Title",
            priority=Task.Priority.LOW,
        )

    def test_user_can_update_own_task(self):
        response = self.client.post(
            reverse(
                "tasks:update",
                kwargs={"task_id": self.task.pk},
            ),
            {
                "title": "Updated Task Title",
                "description": "Updated description",
                "priority": Task.Priority.HIGH,
                "due_date": "",
            },
        )

        self.assertRedirects(
            response,
            reverse(
                "tasks:detail",
                kwargs={"task_id": self.task.pk},
            ),
        )

        self.task.refresh_from_db()

        self.assertEqual(self.task.title, "Updated Task Title")
        self.assertEqual(self.task.priority, Task.Priority.HIGH)


class TaskDeleteViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="deleteuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.task = Task.objects.create(
            user=self.user,
            title="Task to Delete",
        )

    def test_user_can_view_delete_confirmation(self):
        response = self.client.get(
            reverse(
                "tasks:delete",
                kwargs={"task_id": self.task.pk},
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_user_can_delete_own_task(self):
        response = self.client.post(
            reverse(
                "tasks:delete",
                kwargs={"task_id": self.task.pk},
            )
        )

        self.assertRedirects(response, reverse("tasks:list"))

        self.assertFalse(
            Task.objects.filter(pk=self.task.pk).exists()
        )


class TaskCompletionViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="completionuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.task = Task.objects.create(
            user=self.user,
            title="Complete Django Project",
            completed=False,
        )

    def test_user_can_mark_task_as_completed(self):
        response = self.client.post(
            reverse(
                "tasks:toggle_complete",
                kwargs={"task_id": self.task.pk},
            )
        )

        self.assertRedirects(response, reverse("tasks:list"))

        self.task.refresh_from_db()

        self.assertTrue(self.task.completed)

    def test_user_can_mark_completed_task_as_pending(self):
        self.task.completed = True
        self.task.save()

        response = self.client.post(
            reverse(
                "tasks:toggle_complete",
                kwargs={"task_id": self.task.pk},
            )
        )

        self.assertRedirects(response, reverse("tasks:list"))

        self.task.refresh_from_db()

        self.assertFalse(self.task.completed)

    def test_toggle_completion_rejects_get_request(self):
        response = self.client.get(
            reverse(
                "tasks:toggle_complete",
                kwargs={"task_id": self.task.pk},
            )
        )

        self.assertEqual(response.status_code, 405)
