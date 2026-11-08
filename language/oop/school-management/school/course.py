from .student import Student
from .teacher import Teacher
from .validators import validate_name


class Course:
    """References independently created students and a teacher."""

    def __init__(self, course_id: str, name: str):
        self.__course_id = validate_name(course_id, "Course ID")
        self.__name = validate_name(name, "Course name")
        self.__students: dict[str, Student] = {}
        self.__teacher: Teacher | None = None

    @property
    def course_id(self) -> str:
        return self.__course_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def students(self) -> tuple[Student, ...]:
        return tuple(self.__students.values())

    @property
    def teacher(self) -> Teacher | None:
        return self.__teacher

    def enroll_student(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError("student must be a Student instance.")
        if student.student_id in self.__students:
            raise ValueError(
                f"Student {student.student_id!r} is already enrolled in {self.name!r}."
            )
        self.__students[student.student_id] = student

    def withdraw_student(self, student: Student | str) -> None:
        student_id = student.student_id if isinstance(student, Student) else student
        if not isinstance(student_id, str):
            raise TypeError("Provide a Student object or student ID string.")
        if student_id not in self.__students:
            raise KeyError(f"Student {student_id!r} is not enrolled in {self.name!r}.")
        del self.__students[student_id]

    def assign_teacher(self, teacher: Teacher) -> None:
        if not isinstance(teacher, Teacher):
            raise TypeError("teacher must be a Teacher instance.")
        self.__teacher = teacher

    def __repr__(self) -> str:
        return f"Course({self.course_id!r}, {self.name!r})"
