from .validators import validate_email, validate_name


class Teacher:
    """A teacher exists independently of any School object."""

    def __init__(self, teacher_id: str, name: str, subject: str, email: str):
        self.__teacher_id = validate_name(teacher_id, "Teacher ID")
        self.__name = validate_name(name, "Teacher name")
        self.__subject = validate_name(subject, "Teacher subject")
        self.__email = validate_email(email)

    @property
    def teacher_id(self) -> str:
        return self.__teacher_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def subject(self) -> str:
        return self.__subject

    @property
    def email(self) -> str:
        return self.__email

    def __repr__(self) -> str:
        return f"Teacher({self.teacher_id!r}, {self.name!r})"
