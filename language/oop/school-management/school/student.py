from .validators import validate_email, validate_name, validate_positive_int


class Student:
    """A student exists independently of any School object."""

    def __init__(self, student_id: str, name: str, age: int, email: str):
        self.__student_id = validate_name(student_id, "Student ID")
        self.__name = validate_name(name, "Student name")
        self.__age = validate_positive_int(age, "Student age")
        self.__email = validate_email(email)

    @property
    def student_id(self) -> str:
        return self.__student_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    @property
    def email(self) -> str:
        return self.__email

    def __repr__(self) -> str:
        return f"Student({self.student_id!r}, {self.name!r})"
