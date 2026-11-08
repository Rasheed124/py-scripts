from .validators import validate_name, validate_email

class User:
    """Shared account identity and status behavior."""
    def __init__(self, user_name: str, email: str):
        self.__user_name = validate_name(user_name, "User name")
        self.__email = validate_email(email)
        self.__is_account_active = True

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def email(self) -> str:
        return self.__email

    @property
    def is_account_active(self) -> bool:
        return self.__is_account_active

    def activate_account(self) -> None:
        self.__is_account_active = True

    def deactivate_account(self) -> None:
        self.__is_account_active = False

    def _ensure_active(self) -> None:
        if not self.is_account_active:
            raise PermissionError("This account is deactivated.")

    def display_user_information(self) -> str:
        status = "Active" if self.is_account_active else "Deactivated"
        return (f"\n========== USER INFORMATION ==========\n"
                f"Name: {self.user_name}\nEmail: {self.email}\n"
                f"Account status: {status}\n======================================")

    def __str__(self) -> str:
        return f"User({self.user_name!r}, {self.email!r})"
