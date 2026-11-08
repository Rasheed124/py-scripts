from school import Course, School, Student, Teacher


def main() -> None:
    # Objects are created independently of the School.
    alice = Student("S001", "Alice Johnson", 20, "alice@example.com")
    ben = Student("S002", "Ben Carter", 22, "ben@example.com")
    mary = Student("S003", "Mary James", 19, "mary@example.com")

    teacher_ada = Teacher("T001", "Ada Williams", "Python Programming", "ada@example.com")
    teacher_john = Teacher("T002", "John Smith", "Database Systems", "john@example.com")

    python_course = Course("C001", "Python Programming")
    database_course = Course("C002", "Database Systems")

    # The School registers existing objects; it does not create them.
    school = School("Greenfield Academy")
    for student in (alice, ben, mary):
        school.add_student(student)
    for teacher in (teacher_ada, teacher_john):
        school.add_teacher(teacher)
    for course in (python_course, database_course):
        school.add_course(course)

    python_course.assign_teacher(teacher_ada)
    database_course.assign_teacher(teacher_john)

    python_course.enroll_student(alice)
    python_course.enroll_student(ben)
    database_course.enroll_student(ben)
    database_course.enroll_student(mary)

    print(school.generate_report())

    print("\n=== TEACHER REASSIGNMENT ===")
    python_course.assign_teacher(teacher_john)
    print(f"{python_course.name} is now taught by {python_course.teacher.name}")

    print("\n=== WITHDRAWAL ===")
    python_course.withdraw_student(ben)
    print(f"Students remaining in {python_course.name}: "
          f"{', '.join(student.name for student in python_course.students)}")

    print("\n=== AGGREGATION DEMONSTRATION ===")
    school.remove_student("S001")
    print(f"Alice still exists independently: {alice.name}")
    print(f"Is Alice registered with school? {school.has_student('S001')}")

    print("\n=== INVALID OPERATION TESTS ===")
    try:
        python_course.enroll_student(alice)  # Alice can still be used as an object.
        print("Alice can be enrolled in a course even after registry removal.")
    except (TypeError, ValueError, KeyError) as error:
        print("Enrollment rejected:", error)

    try:
        python_course.enroll_student(alice)
    except ValueError as error:
        print("Duplicate enrollment handled:", error)

    try:
        python_course.assign_teacher("Not a teacher")
    except TypeError as error:
        print("Invalid teacher assignment handled:", error)


if __name__ == "__main__":
    main()
