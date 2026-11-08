from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from datetime import timedelta
from django.utils import timezone

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








class TaskListFeatureTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="listuser",
            password="TestPassword123!",
        )
        self.client.force_login(self.user)

        today = timezone.localdate()

        self.task_today = Task.objects.create(
            user=self.user,
            title="Finish Django project",
            description="Complete the task dashboard.",
            priority=Task.Priority.HIGH,
            due_date=today,
        )

        self.task_upcoming = Task.objects.create(
            user=self.user,
            title="Study Python",
            description="Practise Python functions.",
            priority=Task.Priority.MEDIUM,
            due_date=today + timedelta(days=3),
        )

        self.task_overdue = Task.objects.create(
            user=self.user,
            title="Submit assignment",
            description="Finish the outstanding assignment.",
            priority=Task.Priority.LOW,
            due_date=today - timedelta(days=2),
        )

        self.task_completed = Task.objects.create(
            user=self.user,
            title="Read Django documentation",
            description="Documentation revision.",
            priority=Task.Priority.HIGH,
            completed=True,
            due_date=today - timedelta(days=1),
        )

        base_time = timezone.now()

        for index, task in enumerate([
            self.task_today,
            self.task_upcoming,
            self.task_overdue,
            self.task_completed,
        ]):
            Task.objects.filter(pk=task.pk).update(
                created_at=base_time + timedelta(seconds=index)
            )



    def get_task_ids(self, response):
        return [
            task.pk
            for task in response.context["page_obj"].object_list
        ]
    def test_search_finds_task_by_title(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"q": "Django project"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.get_task_ids(response),
            [self.task_today.pk],
        )

    def test_search_finds_task_by_description(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"q": "Python functions"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            self.get_task_ids(response),
            [self.task_upcoming.pk],
        )

    def test_search_is_case_insensitive(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"q": "DJANGO PROJECT"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [self.task_today.pk],
        )

    def test_completed_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"status": "completed"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [self.task_completed.pk],
        )

    def test_pending_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"status": "pending"},
        )

        task_ids = self.get_task_ids(response)

        self.assertEqual(len(task_ids), 3)
        self.assertNotIn(self.task_completed.pk, task_ids)

    def test_priority_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"priority": Task.Priority.HIGH},
        )

        task_ids = self.get_task_ids(response)

        self.assertEqual(
            set(task_ids),
            {self.task_today.pk, self.task_completed.pk},
        )

    def test_today_schedule_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"schedule": "today"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [self.task_today.pk],
        )

    def test_upcoming_schedule_filter(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"schedule": "upcoming"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [self.task_upcoming.pk],
        )

    def test_overdue_schedule_filter_excludes_completed_tasks(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"schedule": "overdue"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [self.task_overdue.pk],
        )

    def test_combined_search_and_filters(self):
        response = self.client.get(
            reverse("tasks:list"),
            {
                "q": "Django",
                "status": "pending",
                "priority": Task.Priority.HIGH,
            },
        )

        self.assertEqual(
            self.get_task_ids(response),
            [self.task_today.pk],
        )

    def test_newest_sorting(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"sort": "newest"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [
                self.task_completed.pk,
                self.task_overdue.pk,
                self.task_upcoming.pk,
            ],
        )

    def test_oldest_sorting(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"sort": "oldest"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [
                self.task_today.pk,
                self.task_upcoming.pk,
                self.task_overdue.pk,
            ],
        )

    def test_high_priority_sorting(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"sort": "priority_high"},
        )

        task_ids = self.get_task_ids(response)

        self.assertEqual(
            task_ids[:2],
            [self.task_completed.pk, self.task_today.pk],
        )

    def test_low_priority_sorting(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"sort": "priority_low"},
        )

        task_ids = self.get_task_ids(response)

        self.assertEqual(task_ids[0], self.task_overdue.pk)

    def test_due_earliest_sorting(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"sort": "due_earliest"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [
                self.task_overdue.pk,
                self.task_completed.pk,
                self.task_today.pk,
            ],
        )

    def test_due_latest_sorting(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"sort": "due_latest"},
        )

        self.assertEqual(
            self.get_task_ids(response),
            [
                self.task_upcoming.pk,
                self.task_today.pk,
                self.task_completed.pk,
            ],
        )

    def test_dashboard_statistics_are_not_affected_by_filters(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"status": "completed"},
        )

        self.assertEqual(response.context["total_tasks"], 4)
        self.assertEqual(response.context["completed_tasks"], 1)
        self.assertEqual(response.context["pending_tasks"], 3)
        self.assertEqual(response.context["overdue_tasks"], 1)
        self.assertEqual(response.context["completion_rate"], 25)

    def test_invalid_priority_does_not_filter_tasks(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"priority": "urgent"},
        )

        self.assertEqual(response.context["total_tasks"], 4)

    def test_empty_query_parameter_is_removed(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"q": "   ", "status": "pending"},
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            f"{reverse('tasks:list')}?status=pending",
        )


class TaskPaginationTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="paginationuser",
            password="TestPassword123!",
        )
        self.client.force_login(self.user)

        self.tasks = []

        for number in range(8):
            task = Task.objects.create(
                user=self.user,
                title=f"Pagination Task {number}",
            )
            self.tasks.append(task)

    def test_first_page_contains_three_tasks(self):
        response = self.client.get(reverse("tasks:list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tasks"]), 3)
        self.assertTrue(response.context["page_obj"].has_next())
        self.assertFalse(response.context["page_obj"].has_previous())

    def test_second_page_contains_three_tasks(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"page": 2},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tasks"]), 3)
        self.assertTrue(response.context["page_obj"].has_previous())

    def test_last_page_contains_remaining_tasks(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"page": 3},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["tasks"]), 2)
        self.assertFalse(response.context["page_obj"].has_next())

    def test_invalid_page_number_returns_last_page(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"page": 100},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page_obj"].number, 3)

    def test_non_numeric_page_returns_first_page(self):
        response = self.client.get(
            reverse("tasks:list"),
            {"page": "invalid"},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["page_obj"].number, 1)

    def test_pagination_preserves_other_query_parameters(self):
        response = self.client.get(
            reverse("tasks:list"),
            {
                "page": 2,
                "status": "pending",
                "sort": "oldest",
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["page_base_url"],
            "status=pending&sort=oldest",
        )
