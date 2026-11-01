
from django import forms
from .models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task

        fields = [
            "title",
            "description",
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
            "priority": "Priority",
            "due_date": "Due date",
        }

        help_texts = {
            "title": "Give your task a short, clear title.",
            "due_date": "Optional. Leave empty if there is no deadline.",
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if not title:
            raise forms.ValidationError(
                "Please enter a task title."
            )

        return title
