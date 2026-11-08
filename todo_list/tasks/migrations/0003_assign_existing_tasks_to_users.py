
from django.db import migrations


def assign_existing_tasks(apps, schema_editor):
    Task = apps.get_model("tasks", "Task")
    User = apps.get_model("auth", "User")

    database = schema_editor.connection.alias

    unassigned_tasks = Task.objects.using(database).filter(
        user__isnull=True
    )

    if not unassigned_tasks.exists():
        return

    existing_user = (
        User.objects.using(database)
        .filter(username="adeola")
        .first()
    )

    if existing_user is None:
        raise RuntimeError(
            "Cannot assign existing tasks: "
            "the user 'adeola' does not exist."
        )

    unassigned_tasks.update(user_id=existing_user.pk)


def reverse_assign_existing_tasks(apps, schema_editor):
    Task = apps.get_model("tasks", "Task")
    User = apps.get_model("auth", "User")

    database = schema_editor.connection.alias

    existing_user = (
        User.objects.using(database)
        .filter(username="adeola")
        .first()
    )

    if existing_user is None:
        return

    Task.objects.using(database).filter(
        user_id=existing_user.pk
    ).update(user_id=None)


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0002_task_user"),
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.RunPython(
            assign_existing_tasks,
            reverse_assign_existing_tasks,
        ),
    ]
