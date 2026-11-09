from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class Category(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="categories",
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "name"],
                name="unique_category_name_per_user",
            ),
        ]

    def __str__(self):
        return self.name


class Task(models.Model):

    class Priority(models.TextChoices):
        LOW = "low", "Low"
        MEDIUM = "medium", "Medium"
        HIGH = "high", "High"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tasks",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="tasks",
        blank=True,
        null=True,
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    completed = models.BooleanField(default=False)

    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM,
    )

    due_date = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        super().clean()

        if self.user_id and self.category_id:
            category_belongs_to_user = Category.objects.filter(
                pk=self.category_id,
                user_id=self.user_id,
            ).exists()

            if not category_belongs_to_user:
                raise ValidationError({
                    "category": (
                        "You cannot assign a category "
                        "that belongs to another user."
                    )
                })

    def __str__(self):
        return self.title
