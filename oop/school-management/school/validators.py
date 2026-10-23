import re


def validate_name(value: str, field_name: str = "Name") -> str:
    if not isinstance(value, str):
        raise TypeError(f"{field_name} must be a string.")
    value = value.strip()
    if not value:
        raise ValueError(f"{field_name} cannot be empty.")
    return value


def validate_email(value: str) -> str:
    if not isinstance(value, str):
        raise TypeError("Email must be a string.")
    value = value.strip()
    if (
        not value
        or value.count("@") != 1
        or value.startswith("@")
        or value.endswith("@")
        or any(character.isspace() for character in value)
        or "." not in value.split("@")[1]
        or value.endswith(".")
    ):
        raise ValueError("Please provide a valid email address.")
    return value


def validate_username(username: str) -> str:
    if not isinstance(username, str):
        raise TypeError("Username must be a string.")
    username = username.strip()
    if not username:
        raise ValueError("Username cannot be empty.")
    pattern = r"^[A-Za-z][A-Za-z0-9_]{2,19}$"
    if not re.fullmatch(pattern, username):
        raise ValueError(
            "Username must be 3-20 characters, start with a letter, "
            "and contain only letters, digits or underscores."
        )
    return username


def validate_positive_int(value: int, field_name: str = "Value") -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{field_name} must be an integer.")
    if value <= 0:
        raise ValueError(f"{field_name} must be greater than zero.")
    return value
