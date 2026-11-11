from django import forms

from .models import Task, Category


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
            "category",
            "priority",
            "due_date",
        ]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "What needs to be done?",
                "autocomplete": "off",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Add some details about this task...",
                "rows": 4,
            }),
            "category": forms.Select(attrs={
                "class": "form-control",
            }),
            "priority": forms.Select(attrs={
                "class": "form-control",
            }),
            "due_date": forms.DateInput(attrs={
                "class": "form-control",
                "type": "date",
            }),
        }

        labels = {
            "title": "Task title",
            "description": "Description",
            "category": "Category",
            "priority": "Priority",
            "due_date": "Due date",
        }

        help_texts = {
            "title": "Give your task a short, clear title.",
            "due_date": "Optional. Leave empty if there is no deadline.",
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is None or not user.is_authenticated:
            raise ValueError(
                "An authenticated user is required."
            )

        self.fields["category"].queryset = Category.objects.filter(
            user=user
        )


class CategoryForm(forms.ModelForm):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        if user is None or not user.is_authenticated:
            raise ValueError(
                "An authenticated user is required."
            )

        self.user = user

    class Meta:
        model = Category
        fields = ["name", "description"]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter category name",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Describe this category",
            }),
        }

        labels = {
            "name": "Category name",
            "description": "Description",
        }

        help_texts = {
            "name": "Choose a clear name for this category.",
        }



    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        existing = Category.objects.filter(
            user=self.user,
            name__iexact=name,
        )

        if self.instance.pk:
            existing = existing.exclude(
                pk=self.instance.pk
            )

        if existing.exists():
            raise forms.ValidationError(
                "You already have a category with this name."
            )

        return name
