from datetime import timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Task


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

class TaskListFeatureTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="listuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        today = timezone.localdate()

        self.task_one = Task.objects.create(
            user=self.user,
            title="Learn Django",
            description="Study Django ORM",
            priority="high",
            completed=False,
            due_date=today,
        )

        self.task_two = Task.objects.create(
            user=self.user,
            title="Build Portfolio",
            description="Create a developer portfolio",
            priority="medium",
            completed=True,
            due_date=today + timedelta(days=3),
        )

        self.task_three = Task.objects.create(
            user=self.user,
            title="Read Python",
            description="Practice Python fundamentals",
            priority="low",
            completed=False,
            due_date=today - timedelta(days=2),
        )

class TaskAuthorizationTests(TestCase):

    def setUp(self):

        self.user_a = User.objects.create_user(
            username="adeola",
            email="adeola@example.com",
            password="TestPassword123!",
        )

        self.user_b = User.objects.create_user(
            username="john",
            email="john@example.com",
            password="TestPassword123!",
        )

        self.task_a = Task.objects.create(
            user=self.user_a,
            title="Learn Django",
            description="Study Django authorization",
            priority=Task.Priority.HIGH,
        )

        self.task_a_completed = Task.objects.create(
            user=self.user_a,
            title="Build Portfolio",
            description="Create a developer portfolio",
            priority=Task.Priority.MEDIUM,
            completed=True,
        )

        self.task_b = Task.objects.create(
            user=self.user_b,
            title="Study Python",
            description="Practice Python fundamentals",
            priority=Task.Priority.LOW,
        )

        self.task_b_completed = Task.objects.create(
            user=self.user_b,
            title="Prepare Report",
            description="Complete the project report",
            priority=Task.Priority.MEDIUM,
            completed=True,
        )

    def test_user_sees_only_their_own_tasks(self):
        self.client.force_login(self.user_a)

        response = self.client.get(reverse("tasks:list"))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Learn Django")
        self.assertContains(response, "Build Portfolio")

        self.assertNotContains(response, "Study Python")
        self.assertNotContains(response, "Prepare Report")

    def test_user_cannot_view_another_users_task(self):
        self.client.force_login(self.user_a)

        response = self.client.get(
            reverse(
                "tasks:detail",
                kwargs={"task_id": self.task_b.pk},
            )
        )

        self.assertEqual(response.status_code, 404)

    def test_user_cannot_update_another_users_task(self):
        self.client.force_login(self.user_a)

        response = self.client.post(
            reverse(
                "tasks:update",
                kwargs={"task_id": self.task_b.pk},
            ),
            {
                "title": "Modified by Adeola",
                "description": "Unauthorized modification",
                "priority": Task.Priority.HIGH,
                "due_date": "",
            },
        )

        self.assertEqual(response.status_code, 404)

        self.task_b.refresh_from_db()

        self.assertEqual(
            self.task_b.title,
            "Study Python",
        )

    def test_user_cannot_delete_another_users_task(self):
        self.client.force_login(self.user_a)

        response = self.client.post(
            reverse(
                "tasks:delete",
                kwargs={"task_id": self.task_b.pk},
            )
        )

        self.assertEqual(response.status_code, 404)

        self.assertTrue(
            Task.objects.filter(pk=self.task_b.pk).exists()
        )

    def test_user_cannot_toggle_another_users_task(self):
        self.client.force_login(self.user_a)

        response = self.client.post(
            reverse(
                "tasks:toggle_complete",
                kwargs={"task_id": self.task_b.pk},
            )
        )

        self.assertEqual(response.status_code, 404)

        self.task_b.refresh_from_db()

        self.assertFalse(self.task_b.completed)

    def test_new_task_is_assigned_to_authenticated_user(self):
        self.client.force_login(self.user_a)

        response = self.client.post(
            reverse("tasks:create"),
            {
                "title": "Learn Django Testing",
                "description": "Practice automated tests",
                "priority": Task.Priority.HIGH,
                "due_date": "",
            },
        )

        self.assertRedirects(
            response,
            reverse("tasks:list"),
        )

        new_task = Task.objects.get(
            title="Learn Django Testing"
        )

        self.assertEqual(new_task.user, self.user_a)

    def test_dashboard_statistics_are_user_specific(self):
        self.client.force_login(self.user_a)

        response = self.client.get(reverse("tasks:list"))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.context["total_tasks"], 2)
        self.assertEqual(response.context["completed_tasks"], 1)
        self.assertEqual(response.context["pending_tasks"], 1)

    def test_unauthenticated_user_cannot_access_task_pages(self):
        protected_urls = [
            reverse("tasks:list"),
            reverse("tasks:create"),
            reverse(
                "tasks:detail",
                kwargs={"task_id": self.task_a.pk},
            ),
            reverse(
                "tasks:update",
                kwargs={"task_id": self.task_a.pk},
            ),
            reverse(
                "tasks:delete",
                kwargs={"task_id": self.task_a.pk},
            ),
        ]

        for url in protected_urls:
            with self.subTest(url=url):
                response = self.client.get(url)

                self.assertRedirects(
                    response,
                    f"{reverse('accounts:login')}?next={url}",
                )

    def test_unauthenticated_user_cannot_toggle_completion(self):
        response = self.client.post(
            reverse(
                "tasks:toggle_complete",
                kwargs={"task_id": self.task_a.pk},
            )
        )

        expected_redirect = (
            f"{reverse('accounts:login')}"
            f"?next={reverse('tasks:toggle_complete', kwargs={'task_id': self.task_a.pk})}"
        )

        self.assertRedirects(response, expected_redirect)

        self.task_a.refresh_from_db()

        self.assertFalse(self.task_a.completed)

