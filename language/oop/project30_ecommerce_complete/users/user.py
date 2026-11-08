from uuid import uuid4
from validators import validate_non_empty_string, validate_email, validate_phone


class User:
    def __init__(self, name, email, phone, password):
        self._user_id = str(uuid4())
        self.name = name
        self.email = email
        self.phone = phone
        self._password = self._validate_password(password)
        self._is_active = True

    @staticmethod
    def _validate_password(value):
        if not isinstance(value, str) or len(value) < 8:
            raise ValueError("Password must be at least 8 characters.")
        return value

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = validate_non_empty_string(value, "Name")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = validate_email(value)

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = validate_phone(value)

    @property
    def is_active(self):
        return self._is_active

    def change_password(self, current_password, new_password):
        if current_password != self._password:
            raise ValueError("Current password is incorrect.")
        self._password = self._validate_password(new_password)

    def deactivate(self):
        self._is_active = False

    def activate(self):
        self._is_active = True

    def get_details(self):
        return {"user_id": self.user_id, "name": self.name, "email": self.email,
                "phone": self.phone, "is_active": self.is_active}

    def __str__(self):
        return f"{self.name} <{self.email}>"

    def __repr__(self):
        return f"{type(self).__name__}(user_id={self.user_id!r}, name={self.name!r})"
