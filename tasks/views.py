from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.db.models import Case, When, Value, IntegerField, Count
from django.db.models import Q

from .models import Task
from .forms import TaskForm




from django.shortcuts import render, redirect
from django.db.models import Q, Case, When, Value, IntegerField
from django.utils import timezone
from django.core.paginator import Paginator

from .models import Task


def task_list(request):

    params = request.GET.copy()

    for key in list(params.keys()):
        if not params.get(key, "").strip():
            params.pop(key)

    if params.urlencode() != request.GET.urlencode():
        if params:
            return redirect(f"{request.path}?{params.urlencode()}")

        return redirect(request.path)



    query = request.GET.get("q", "").strip()
    status = request.GET.get("status", "")
    priority = request.GET.get("priority", "")
    sort = request.GET.get("sort", "newest")
    schedule = request.GET.get("schedule", "")
    today = timezone.localdate()

    tasks = Task.objects.all()

    if query:
        tasks = tasks.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )

    if status == "completed":
        tasks = tasks.filter(completed=True)

    elif status == "pending":
        tasks = tasks.filter(completed=False)



    if priority in Task.Priority.values:
        tasks = tasks.filter(priority=priority)

    if schedule == "today":
        tasks = tasks.filter(due_date=today)

    elif schedule == "upcoming":
        tasks = tasks.filter(due_date__gt=today)

    elif schedule == "overdue":
        tasks = tasks.filter(
            due_date__lt=today,
            completed=False
        )

    sort_options = {
        "newest": ("-created_at",),
        "oldest": ("created_at",),
        "due_earliest": ("due_date", "-created_at"),
        "due_latest": ("-due_date", "-created_at"),
    }

    priority_order = Case(
        When(priority="high", then=Value(1)),
        When(priority="medium", then=Value(2)),
        When(priority="low", then=Value(3)),
        output_field=IntegerField(),
    )


    if sort == "priority_high":
        tasks = tasks.order_by(
            priority_order,
            "-created_at"
        )

    elif sort == "priority_low":
        tasks = tasks.order_by(
            priority_order.desc(),
            "-created_at"
        )

    else:
        tasks = tasks.order_by(
            *sort_options.get(sort, sort_options["newest"])
        )


    paginator = Paginator(tasks, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    pagination_params = request.GET.copy()
    pagination_params.pop("page", None)
    page_base_url = pagination_params.urlencode()


    
    # Dashboard statistics
    stats = Task.objects.aggregate(
        total_count=Count("id"),
        completed_count=Count(
            "id",
            filter=Q(completed=True)
        ),
        pending_count=Count(
            "id",
            filter=Q(completed=False)
        ),
        overdue_count=Count(
            "id",
            filter=Q(
                due_date__lt=today,
                completed=False
            )
        ),
    )

    # Calculate completion rate
    completion_rate = (
        (stats["completed_count"] / stats["total_count"]) * 100
        if stats["total_count"] > 0
        else 0
    )


    # 9. Dashboard statistics
    context = {
        "tasks": page_obj,
        "page_obj": page_obj,
        "page_base_url": page_base_url,
        "query": query,
        "status": status,
        "priority": priority,
        "sort": sort,
        "schedule": schedule,
        "today": today,
        "total_tasks": stats["total_count"],
        "completed_tasks": stats["completed_count"],
        "pending_tasks": stats["pending_count"],
        "overdue_tasks": stats["overdue_count"],
        "completion_rate": round(completion_rate),
            }

    return render(request, "tasks/task_list.html", context)



def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tasks:list")
    else:
        form = TaskForm()

    return render(
        request,
        "tasks/task_form.html",
        {"form": form},
    )


def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            return redirect("tasks:detail", task_id=task.pk)
    else:
        form = TaskForm(instance=task)

    return render(
        request,
        "tasks/task_form.html",
        {
            "form": form,
            "task": task,
        },
    )

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    context = {
        "task": task,
    }

    return render(request, "tasks/task_detail.html", context)



@require_http_methods(["GET", "POST"])
def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        task.delete()
        return redirect("tasks:list")

    return render(
        request,
        "tasks/task_confirm_delete.html",
        {"task": task},
    )


@require_POST
def task_toggle_complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    task.completed = not task.completed
    task.save(update_fields=["completed", "updated_at"])

    return redirect("tasks:list")



