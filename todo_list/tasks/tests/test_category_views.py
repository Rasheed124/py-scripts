
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from tasks.models import Category, Task


User = get_user_model()


class CategoryListViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="categorylistuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.category = Category.objects.create(
            user=self.user,
            name="Work",
        )

        self.task = Task.objects.create(
            user=self.user,
            category=self.category,
            title="Complete project",
        )

        self.uncategorized_task = Task.objects.create(
            user=self.user,
            title="Read documentation",
        )

    def test_category_list_returns_200(self):
        response = self.client.get(
            reverse("tasks:category_list")
        )

        self.assertEqual(response.status_code, 200)

    def test_category_list_displays_own_categories(self):
        response = self.client.get(
            reverse("tasks:category_list")
        )

        self.assertContains(response, "Work")
        self.assertEqual(response.context["total_categories"], 1)

    def test_category_list_displays_category_task_count(self):
        response = self.client.get(
            reverse("tasks:category_list")
        )

        category = response.context["categories"].get(
            pk=self.category.pk
        )

        self.assertEqual(category.task_count, 1)

    def test_category_list_displays_task_statistics(self):
        response = self.client.get(
            reverse("tasks:category_list")
        )

        self.assertEqual(
            response.context["categorized_tasks"],
            1,
        )

        self.assertEqual(
            response.context["uncategorized_tasks"],
            1,
        )


class CategoryCreateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="categorycreateuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

    def test_category_create_page_returns_200(self):
        response = self.client.get(
            reverse("tasks:category_create")
        )

        self.assertEqual(response.status_code, 200)

    def test_user_can_create_category(self):
        response = self.client.post(
            reverse("tasks:category_create"),
            {
                "name": "Personal",
                "description": "Personal activities.",
            },
        )

        self.assertRedirects(
            response,
            reverse("tasks:category_list"),
        )

        category = Category.objects.get(name="Personal")

        self.assertEqual(category.user, self.user)

    def test_category_creation_rejects_empty_name(self):
        response = self.client.post(
            reverse("tasks:category_create"),
            {
                "name": "",
                "description": "",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Category.objects.count(), 0)
        self.assertIn("name", response.context["form"].errors)


class CategoryUpdateViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="categoryupdateuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.category = Category.objects.create(
            user=self.user,
            name="Old Category",
        )

    def test_user_can_view_category_update_page(self):
        response = self.client.get(
            reverse(
                "tasks:category_update",
                kwargs={"category_id": self.category.pk},
            )
        )

        self.assertEqual(response.status_code, 200)

    def test_user_can_update_own_category(self):
        response = self.client.post(
            reverse(
                "tasks:category_update",
                kwargs={"category_id": self.category.pk},
            ),
            {
                "name": "Updated Category",
                "description": "Updated description.",
            },
        )

        self.assertRedirects(
            response,
            reverse("tasks:category_list"),
        )

        self.category.refresh_from_db()

        self.assertEqual(
            self.category.name,
            "Updated Category",
        )


class CategoryDeleteViewTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="categorydeleteuser",
            password="TestPassword123!",
        )

        self.client.force_login(self.user)

        self.category = Category.objects.create(
            user=self.user,
            name="Category to Delete",
        )

        self.task = Task.objects.create(
            user=self.user,
            category=self.category,
            title="Task in category",
        )

    def test_user_can_view_category_delete_confirmation(self):
        response = self.client.get(
            reverse(
                "tasks:category_delete",
                kwargs={"category_id": self.category.pk},
            )
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["task_count"], 1)

    def test_user_can_delete_own_category(self):
        response = self.client.post(
            reverse(
                "tasks:category_delete",
                kwargs={"category_id": self.category.pk},
            )
        )

        self.assertRedirects(
            response,
            reverse("tasks:category_list"),
        )

        self.assertFalse(
            Category.objects.filter(
                pk=self.category.pk
            ).exists()
        )

    def test_deleting_category_does_not_delete_its_tasks(self):
        self.client.post(
            reverse(
                "tasks:category_delete",
                kwargs={"category_id": self.category.pk},
            )
        )

        self.task.refresh_from_db()

        self.assertIsNone(self.task.category)
        self.assertTrue(
            Task.objects.filter(pk=self.task.pk).exists()
        )
