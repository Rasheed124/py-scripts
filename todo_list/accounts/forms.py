from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]

    def clean_email(self):
        email = self.cleaned_data["email"].strip()

        email_exists = User.objects.filter(
            email__iexact=email
        ).exists()

        if email_exists:
            raise forms.ValidationError(
                "An account with this email address already exists."
            )

        return email
