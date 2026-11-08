
from django.contrib.auth import get_user_model
from django.test import TestCase

from tasks.forms import TaskForm, CategoryForm
from tasks.models import Category, Task


User = get_user_model()


class TaskFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="formuser",
            password="TestPassword123!",
        )

        self.other_user = User.objects.create_user(
            username="otherformuser",
            password="TestPassword123!",
        )

        self.category = Category.objects.create(
            user=self.user,
            name="Work",
        )

        self.other_category = Category.objects.create(
            user=self.other_user,
            name="Personal",
        )

    def valid_data(self, **overrides):
        data = {
            "title": "Complete Django project",
            "description": "Finish the application.",
            "category": "",
            "priority": Task.Priority.MEDIUM,
            "due_date": "",
        }
        data.update(overrides)
        return data

    def test_valid_task_form(self):
        form = TaskForm(
            data=self.valid_data(),
            user=self.user,
        )

        self.assertTrue(form.is_valid())

    def test_task_form_requires_title(self):
        form = TaskForm(
            data=self.valid_data(title=""),
            user=self.user,
        )

        self.assertFalse(form.is_valid())
        self.assertIn("title", form.errors)

    def test_task_form_only_displays_own_categories(self):
        form = TaskForm(user=self.user)

        category_ids = list(
            form.fields["category"].queryset.values_list(
                "id",
                flat=True,
            )
        )

        self.assertIn(self.category.pk, category_ids)
        self.assertNotIn(self.other_category.pk, category_ids)

    def test_task_form_rejects_another_users_category(self):
        form = TaskForm(
            data=self.valid_data(
                category=self.other_category.pk,
            ),
            user=self.user,
        )

        self.assertFalse(form.is_valid())
        self.assertIn("category", form.errors)

    def test_task_form_accepts_own_category(self):
        form = TaskForm(
            data=self.valid_data(category=self.category.pk),
            user=self.user,
        )

        self.assertTrue(form.is_valid())


class CategoryFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="categoryformuser",
            password="TestPassword123!",
        )

        self.category = Category.objects.create(
            user=self.user,
            name="Work",
            description="Work-related tasks.",
        )

    def test_valid_category_form(self):
        form = CategoryForm(
            data={
                "name": "Personal",
                "description": "Personal tasks.",
            },
            user=self.user,
        )

        self.assertTrue(form.is_valid())

    def test_category_form_rejects_duplicate_name(self):
        form = CategoryForm(
            data={
                "name": "Work",
                "description": "",
            },
            user=self.user,
        )

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_category_form_rejects_case_insensitive_duplicate(self):
        form = CategoryForm(
            data={
                "name": "work",
                "description": "",
            },
            user=self.user,
        )

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_category_form_allows_unchanged_name_during_update(self):
        form = CategoryForm(
            data={
                "name": "Work",
                "description": "Updated description.",
            },
            instance=self.category,
            user=self.user,
        )

        self.assertTrue(form.is_valid())

    def test_category_form_allows_another_users_same_name(self):
        other_user = User.objects.create_user(
            username="differentcategoryuser",
            password="TestPassword123!",
        )

        form = CategoryForm(
            data={
                "name": "Work",
                "description": "",
            },
            user=other_user,
        )

        self.assertTrue(form.is_valid())
