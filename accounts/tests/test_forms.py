
from django.contrib.auth import get_user_model
from django.test import TestCase

from accounts.forms import RegistrationForm


User = get_user_model()


class RegistrationFormTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="existinguser",
            email="existing@example.com",
            password="TestPassword123!",
        )

    def valid_data(self, **overrides):
        data = {
            "username": "newuser",
            "email": "new@example.com",
            "password1": "StrongPassword123!",
            "password2": "StrongPassword123!",
        }
        data.update(overrides)
        return data

    def test_valid_registration_form(self):
        form = RegistrationForm(data=self.valid_data())

        self.assertTrue(form.is_valid())

    def test_registration_rejects_duplicate_email(self):
        form = RegistrationForm(
            data=self.valid_data(
                email="existing@example.com",
            )
        )

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_registration_rejects_case_insensitive_duplicate_email(self):
        form = RegistrationForm(
            data=self.valid_data(
                email="EXISTING@example.com",
            )
        )

        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_registration_rejects_mismatched_passwords(self):
        form = RegistrationForm(
            data=self.valid_data(
                password2="DifferentPassword123!",
            )
        )

        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)
