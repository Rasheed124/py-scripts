from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path("", views.task_list, name="list"),
    path("create/", views.task_create, name="create"),
    path("<int:task_id>/", views.task_detail, name="detail"),
    path("<int:task_id>/edit/", views.task_update, name="update"),
    path("<int:task_id>/delete/", views.task_delete, name="delete"),
    path(
        "<int:task_id>/toggle-complete/",
        views.task_toggle_complete,
        name="toggle_complete",
    ),

    path("categories/", views.category_list, name="category_list"),
    path("categories/create/", views.category_create, name="category_create"),
    path(
        "categories/<int:category_id>/edit/",
        views.category_update,
        name="category_update",
    ),
    path(
        "categories/<int:category_id>/delete/",
        views.category_delete,
        name="category_delete",
    ),
]

