# Problem 26 — Aggregation: School Management System

## Structure

    project26_school/
    ├── main.py
    └── school/
        ├── __init__.py
        ├── validators.py
        ├── student.py
        ├── teacher.py
        ├── course.py
        └── school.py

## Run

From the project root, run:

    python main.py

## Design notes

- Student and Teacher objects are created independently of School.
- School stores references to registered students, teachers, and courses.
- Course stores references to enrolled Student objects and its assigned Teacher.
- Removing a reference from a School or Course does not destroy the original object.
- Duplicate IDs and duplicate enrollment are rejected.
- Invalid teacher/student types and missing removals are handled with clear exceptions.
