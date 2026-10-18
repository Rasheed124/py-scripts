from uuid import uuid4


class Person:
    def __init__(self, name: str, age: int):
        if not isinstance(name, str):
            raise TypeError("Person name must be a string.")

        if not name.strip():
            raise ValueError("Person name cannot be empty.")

        self.__name = name.strip()
        self.__age = self._to_int(age)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def age(self) -> int:
        return self.__age

    def display_personal_details(self) -> str:
        return (
            f"Person Name: {self.name}\n"
            f"Person Age: {self.age}\n"
        )

    @staticmethod
    def _to_int(age: int) -> int:
        if isinstance(age, bool) or not isinstance(age, int):
            raise TypeError("Age must be an integer.")

        if age <= 0:
            raise ValueError("Age must be greater than zero.")

        return age

    @staticmethod
    def _to_str(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("Value must be a string.")

        if not value.strip():
            raise ValueError("Value cannot be empty.")

        return value.strip()


class Student(Person):
    def __init__(
        self,
        name: str,
        age: int,
        course: str,
        department: str,
    ):
        super().__init__(name, age)

        self.__course = self._to_str(course)
        self.__department = self._to_str(department)
        self.__student_id = f"Stud-{uuid4().hex[:12].upper()}"

    @property
    def student_id(self) -> str:
        return self.__student_id

    @property
    def student_course(self) -> str:
        return self.__course

    @property
    def student_department(self) -> str:
        return self.__department

def display_personal_details(self) -> str:
    details = super().display_personal_details()

    return (
        details
        + f"Student ID: {self.student_id}\n"
        + f"Student Course: {self.student_course}\n"
        + f"Student Department: {self.student_department}\n"
    )


class GraduateStudent(Student):
    def __init__(
        self,
        name: str,
        age: int,
        course: str,
        department: str,
        research_topic: str,
        supervisor_name: str,
    ):
        super().__init__(name, age, course, department)

        self.__research_topic = self._to_str(research_topic)
        self.__supervisor_name = self._to_str(supervisor_name)

    @property
    def graduate_student_research_topic(self) -> str:
        return self.__research_topic

    @property
    def graduate_student_supervisor_name(self) -> str:
        return self.__supervisor_name

    def display_personal_details(self) -> str:
        return (
            f"Graduate Student ID: {self.student_id}\n"
            f"Graduate Student Name: {self.name}\n"
            f"Graduate Student Age: {self.age}\n"
            f"Graduate Student Course: {self.student_course}\n"
            f"Graduate Student Department: {self.student_department}\n"
            f"Graduate Student Supervisor Name: "
            f"{self.graduate_student_supervisor_name}\n"
            f"Graduate Student Research Topic: "
            f"{self.graduate_student_research_topic}\n"
        )


student = Student(
    "John Doe",
    25,
    "Computer Science",
    "Computing",
)

graduate = GraduateStudent(
    "Jane Doe",
    26,
    "Computer Science",
    "Computing",
    "Artificial Intelligence",
    "Dr. Smith",
)


print(issubclass(GraduateStudent, Student))  
print(issubclass(Student, Person))           
print(issubclass(GraduateStudent, Person))   

print(isinstance(student, Person))           
print(isinstance(graduate, GraduateStudent)) 
print(isinstance(graduate, Student))         
print(isinstance(graduate, Person))          


print("\n--- Student Details ---")
print(student.display_personal_details())

print("--- Graduate Student Details ---")
print(graduate.display_personal_details())