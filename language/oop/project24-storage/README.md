# Problem 24 — Abstract File Storage System

## Structure

    project24_storage/
    ├── main.py
    ├── README.md
    └── storage/
        ├── __init__.py
        ├── base.py
        ├── local_storage.py
        ├── memory_storage.py
        └── user_service.py

## Run

From the project root, run:

    python main.py

Do not run storage/user_service.py directly; it uses package-relative imports.

## Behavior

- Storage defines abstract save, get, and delete operations.
- MemoryStorage stores data in a dictionary.
- LocalStorage stores each record as a JSON file under data/.
- UserService receives a storage implementation and does not depend on its internal details.
- Missing records raise KeyError; invalid keys raise TypeError or ValueError.
- LocalStorage accepts JSON-serializable data only.
