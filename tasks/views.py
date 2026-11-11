
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import ( Case, When, Value, IntegerField, Count, Q,
)
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.decorators.http import require_POST, require_http_methods, require_GET, require_http_methods

from .forms import TaskForm, CategoryForm
from .models import Task, Category

TASKS_PER_PAGE = 3


@login_required
@require_GET
def task_list(request):

    user_tasks = Task.objects.filter(user=request.user)
    tasks = user_tasks


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

    # Search.
    if query:
        tasks = tasks.filter(
            Q(title__icontains=query)
            | Q(description__icontains=query)
        )

    # Status filtering.
    if status == "completed":
        tasks = tasks.filter(completed=True)
    elif status == "pending":
        tasks = tasks.filter(completed=False)

    # Priority filtering.
    if priority in Task.Priority.values:
        tasks = tasks.filter(priority=priority)

    # Schedule filtering.
    if schedule == "today":
        tasks = tasks.filter(due_date=today)
    elif schedule == "upcoming":
        tasks = tasks.filter(due_date__gt=today)
    elif schedule == "overdue":
        tasks = tasks.filter(
            due_date__lt=today,
            completed=False,
        )

    # Sorting.
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
            "-created_at",
        )
    elif sort == "priority_low":
        tasks = tasks.order_by(
            priority_order.desc(),
            "-created_at",
        )
    else:
        tasks = tasks.order_by(
            *sort_options.get(sort, sort_options["newest"])
        )

    # Pagination.
    paginator = Paginator(tasks, TASKS_PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    pagination_params = request.GET.copy()
    pagination_params.pop("page", None)
    page_base_url = pagination_params.urlencode()

    # User-specific dashboard statistics.
    stats = user_tasks.aggregate(
        total_count=Count("id"),
        completed_count=Count(
            "id",
            filter=Q(completed=True),
        ),
        pending_count=Count(
            "id",
            filter=Q(completed=False),
        ),
        overdue_count=Count(
            "id",
            filter=Q(
                due_date__lt=today,
                completed=False,
            ),
        ),
    )

    completion_rate = (
        stats["completed_count"] / stats["total_count"] * 100
        if stats["total_count"] > 0
        else 0
    )

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


@login_required
@require_http_methods(["GET", "POST"])
def task_create(request):
    if request.method == "POST":
        form = TaskForm(
            request.POST,
            user=request.user,
        )

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user

            task.full_clean()
            task.save()

            return redirect("tasks:list")
    else:
        form = TaskForm(user=request.user)

    return render(
        request,
        "tasks/task_form.html",
        {"form": form},
    )


@login_required
@require_GET
def task_detail(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id,
        user=request.user,
    )

    return render(
        request,
        "tasks/task_detail.html",
        {"task": task},
    )


@login_required
@require_http_methods(["GET", "POST"])
def task_update(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id,
        user=request.user,
    )

    if request.method == "POST":
        form = TaskForm(
            request.POST,
            instance=task,
            user=request.user,
        )

        if form.is_valid():
            form.save()

            return redirect(
                "tasks:detail",
                task_id=task.pk,
            )
    else:
        form = TaskForm(
                instance=task,
                user=request.user,)

    return render(
        request,
        "tasks/task_form.html",
        {"form": form, "task": task},
    )


@login_required
@require_http_methods(["GET", "POST"])
def task_delete(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id,
        user=request.user,
    )

    if request.method == "POST":
        task.delete()
        return redirect("tasks:list")

    return render(
        request,
        "tasks/task_confirm_delete.html",
        {"task": task},
    )


@login_required
@require_POST
def task_toggle_complete(request, task_id):
    task = get_object_or_404(
        Task,
        pk=task_id,
        user=request.user,
    )

    task.completed = not task.completed
    task.save(update_fields=["completed", "updated_at"])

    return redirect("tasks:list")




# ==================================== CATEGORY VIEWS REDERNG =============================================================


@login_required
@require_GET
def category_list(request):
    categories = Category.objects.filter(
        user=request.user
    ).annotate(
        task_count=Count(
            "tasks",
            filter=Q(tasks__user=request.user),
        )
    )

    task_stats = Task.objects.filter(
        user=request.user
    ).aggregate(
        categorized_tasks=Count(
            "id",
            filter=Q(category__isnull=False),
        ),
        uncategorized_tasks=Count(
            "id",
            filter=Q(category__isnull=True),
        ),
    )

    context = {
        "categories": categories,
        "total_categories": categories.count(),
        **task_stats,
    }

    return render(
        request,
        "tasks/categories/category_list.html",
        context,
    )



@login_required
@require_http_methods(["GET", "POST"])
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(
            request.POST,
            user=request.user,
        )

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()

            return redirect("tasks:category_list")

    else:
        form = CategoryForm(user=request.user)

    return render(
        request,
        "tasks/categories/category_form.html",
        {"form": form},
    )


@login_required
@require_http_methods(["GET", "POST"])
def category_update(request, category_id):
    category = get_object_or_404(
        Category,
        pk=category_id,
        user=request.user,
    )

    if request.method == "POST":
        form = CategoryForm(
            request.POST,
            instance=category,
            user=request.user,
        )

        if form.is_valid():
            form.save()
            return redirect("tasks:category_list")

    else:
        form = CategoryForm(
            instance=category,
            user=request.user,
        )

    return render(
        request,
        "tasks/categories/category_form.html",
        {
            "form": form,
            "category": category,
        },
    )


@login_required
@require_http_methods(["GET", "POST"])
def category_delete(request, category_id):
    category = get_object_or_404(
        Category,
        pk=category_id,
        user=request.user,
    )

    task_count = category.tasks.count()


    context = {
        "category": category,
        "task_count": task_count,
    }

    if request.method == "POST":
        category.delete()
        return redirect("tasks:category_list")

    return render(
        request,
        "tasks/categories/category_confirm_delete.html",
        context,
    )
