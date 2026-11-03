from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from django.db.models import Q

from .models import Task
from .forms import TaskForm




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

    tasks = tasks.order_by("-created_at")

    context = {
        "tasks": tasks,
        "query": query,
        "status": status,
            "priority": priority,
        "total_tasks": Task.objects.count(),
        "completed_tasks": Task.objects.filter(completed=True).count(),
        "pending_tasks": Task.objects.filter(completed=False).count(),
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



