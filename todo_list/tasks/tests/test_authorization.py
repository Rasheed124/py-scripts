from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Task


User = get_user_model()


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

        self.assertEqual(self.task_b.title, "Study Python")

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











from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Category, Task


User = get_user_model()


class CategoryAuthorizationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="categoryowner",
            password="TestPassword123!",
        )

        self.other_user = User.objects.create_user(
            username="othercategoryowner",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.other_category = Category.objects.create(
            user=self.other_user,
            name="Private Category",
        )

    def test_user_cannot_update_another_users_category(self):
        response = self.client.post(
            reverse(
                "tasks:category_update",
                kwargs={"category_id": self.other_category.pk},
            ),
            {
                "name": "Modified Category",
                "description": "",
            },
        )

        self.assertEqual(response.status_code, 404)

        self.other_category.refresh_from_db()

        self.assertEqual(
            self.other_category.name,
            "Private Category",
        )

    def test_user_cannot_delete_another_users_category(self):
        response = self.client.post(
            reverse(
                "tasks:category_delete",
                kwargs={"category_id": self.other_category.pk},
            )
        )

        self.assertEqual(response.status_code, 404)

        self.assertTrue(
            Category.objects.filter(
                pk=self.other_category.pk
            ).exists()
        )

    def test_category_list_does_not_show_another_users_categories(self):
        response = self.client.get(
            reverse("tasks:category_list")
        )

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Private Category")

    def test_category_create_assigns_authenticated_user(self):
        response = self.client.post(
            reverse("tasks:category_create"),
            {
                "name": "My Category",
                "description": "",
            },
        )

        self.assertRedirects(
            response,
            reverse("tasks:category_list"),
        )

        category = Category.objects.get(name="My Category")

        self.assertEqual(category.user, self.user)


class CrossUserCategoryAssignmentTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="taskowner",
            password="TestPassword123!",
        )

        self.other_user = User.objects.create_user(
            username="categoryowner2",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.other_category = Category.objects.create(
            user=self.other_user,
            name="Other User Category",
        )

    def test_task_creation_rejects_another_users_category(self):
        response = self.client.post(
            reverse("tasks:create"),
            {
                "title": "Attempted task",
                "description": "",
                "category": self.other_category.pk,
                "priority": Task.Priority.MEDIUM,
                "due_date": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            Task.objects.filter(user=self.user).count(),
            0,
        )
        self.assertIn("category", response.context["form"].errors)

    def test_task_update_rejects_another_users_category(self):
        task = Task.objects.create(
            user=self.user,
            title="My task",
        )

        response = self.client.post(
            reverse(
                "tasks:update",
                kwargs={"task_id": task.pk},
            ),
            {
                "title": "My task",
                "description": "",
                "category": self.other_category.pk,
                "priority": Task.Priority.MEDIUM,
                "due_date": "",
            },
        )

        self.assertEqual(response.status_code, 200)

        task.refresh_from_db()

        self.assertIsNone(task.category)
        self.assertIn("category", response.context["form"].errors)
