from .course import Course
from .student import Student
from .teacher import Teacher
from .validators import validate_name


class School:
    """Aggregates references to students, teachers, and courses."""

    def __init__(self, name: str):
        self.__name = validate_name(name, "School name")
        self.__students: dict[str, Student] = {}
        self.__teachers: dict[str, Teacher] = {}
        self.__courses: dict[str, Course] = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def students(self) -> tuple[Student, ...]:
        return tuple(self.__students.values())

    @property
    def teachers(self) -> tuple[Teacher, ...]:
        return tuple(self.__teachers.values())

    @property
    def courses(self) -> tuple[Course, ...]:
        return tuple(self.__courses.values())

    def add_student(self, student: Student) -> None:
        if not isinstance(student, Student):
            raise TypeError("student must be a Student instance.")
        if student.student_id in self.__students:
            raise ValueError(f"Student ID {student.student_id!r} is already registered.")
        self.__students[student.student_id] = student

    def remove_student(self, student_id: str) -> None:
        if student_id not in self.__students:
            raise KeyError(f"Student {student_id!r} is not registered.")
        del self.__students[student_id]

    def has_student(self, student_id: str) -> bool:
        return student_id in self.__students

    def add_teacher(self, teacher: Teacher) -> None:
        if not isinstance(teacher, Teacher):
            raise TypeError("teacher must be a Teacher instance.")
        if teacher.teacher_id in self.__teachers:
            raise ValueError(f"Teacher ID {teacher.teacher_id!r} is already registered.")
        self.__teachers[teacher.teacher_id] = teacher

    def remove_teacher(self, teacher_id: str) -> None:
        if teacher_id not in self.__teachers:
            raise KeyError(f"Teacher {teacher_id!r} is not registered.")
        del self.__teachers[teacher_id]

    def add_course(self, course: Course) -> None:
        if not isinstance(course, Course):
            raise TypeError("course must be a Course instance.")
        if course.course_id in self.__courses:
            raise ValueError(f"Course ID {course.course_id!r} is already registered.")
        self.__courses[course.course_id] = course

    def remove_course(self, course_id: str) -> None:
        if course_id not in self.__courses:
            raise KeyError(f"Course {course_id!r} is not registered.")
        del self.__courses[course_id]

    def generate_report(self) -> str:
        lines = [
            "=" * 55,
            f"SCHOOL REPORT: {self.name}",
            "=" * 55,
            f"Registered students: {len(self.__students)}",
        ]
        for student in self.__students.values():
            lines.append(f"  - {student.student_id}: {student.name} ({student.email})")

        lines.append(f"\nRegistered teachers: {len(self.__teachers)}")
        for teacher in self.__teachers.values():
            lines.append(
                f"  - {teacher.teacher_id}: {teacher.name} — {teacher.subject}"
            )

        lines.append(f"\nCourses: {len(self.__courses)}")
        for course in self.__courses.values():
            teacher_name = course.teacher.name if course.teacher else "Unassigned"
            lines.append(
                f"  - {course.course_id}: {course.name} | Teacher: {teacher_name}"
            )
            if course.students:
                for student in course.students:
                    lines.append(f"      Student: {student.name} ({student.student_id})")
            else:
                lines.append("      No students enrolled.")

        lines.append("=" * 55)
        return "\n".join(lines)
