from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.exceptions import ValidationError


from tasks.models import Task, Category


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




class CategoryRelationshipTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="modeluser",
            password="TestPassword123!",
        )

        self.category = Category.objects.create(
            user=self.user,
            name="Work",
        )

    def test_category_string_representation(self):
        self.assertEqual(str(self.category), "Work")

    def test_deleting_category_sets_task_category_to_null(self):
        task = Task.objects.create(
            user=self.user,
            category=self.category,
            title="Complete work",
        )

        self.category.delete()
        task.refresh_from_db()

        self.assertIsNone(task.category)

    def test_category_name_is_unique_per_user(self):
        category = Category(
            user=self.user,
            name="Work",
        )

        with self.assertRaises(ValidationError):
            category.full_clean()


class TaskCategoryValidationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="taskmodeluser",
            password="TestPassword123!",
        )

        self.other_user = User.objects.create_user(
            username="othermodeluser",
            password="TestPassword123!",
        )

        self.own_category = Category.objects.create(
            user=self.user,
            name="Work",
        )

        self.other_category = Category.objects.create(
            user=self.other_user,
            name="Personal",
        )

    def test_task_accepts_its_users_category(self):
        task = Task(
            user=self.user,
            category=self.own_category,
            title="Valid task",
        )

        task.full_clean()

    def test_task_rejects_another_users_category(self):
        task = Task(
            user=self.user,
            category=self.other_category,
            title="Invalid task",
        )

        with self.assertRaises(ValidationError) as error:
            task.full_clean()

        self.assertIn("category", error.exception.message_dict)
