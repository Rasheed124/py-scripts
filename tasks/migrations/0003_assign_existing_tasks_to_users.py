
from django.db import migrations


def assign_existing_tasks(apps, schema_editor):
    Task = apps.get_model("tasks", "Task")
    User = apps.get_model("auth", "User")

    database = schema_editor.connection.alias

    existing_user = (
        User.objects.using(database)
        .get(username="adeola")
    )

    Task.objects.using(database).filter(
        user__isnull=True
    ).update(user_id=existing_user.pk)


def reverse_assign_existing_tasks(apps, schema_editor):
    Task = apps.get_model("tasks", "Task")

    database = schema_editor.connection.alias

    Task.objects.using(database).filter(
        user__username="adeola"
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
