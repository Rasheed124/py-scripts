import json
import random
import string
from pathlib import Path


class TodoListError(Exception):
    """Base exception for To-Do CLI domain errors."""
    pass


class InvalidInputError(TodoListError):
    """Raised when user input is invalid."""
    pass


class TodoListNotFoundError(TodoListError):
    """Raised when a Todo ID does not exist."""
    pass


class StorageError(TodoListError):
    """Raised when loading or saving JSON data fails."""
    pass


DATA_FILE = Path(__file__).parent / "todo_lists.json"


def load_todo_lists() -> dict:
    """Load todo lists from JSON storage file if it exists."""
    if not DATA_FILE.exists():
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise StorageError(f"Failed to load todo lists from storage: {e}")


def save_todo_lists(content: dict) -> None:
    """Save content dictionary to JSON storage file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        raise StorageError(f"Failed to save todo lists to storage: {e}")


def generate_todo_id(todo_lists: dict) -> str:
    """Generate a unique 8-character alphanumeric ID for a task."""
    while True:
        todo_id = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=8)
        )
        if todo_id not in todo_lists:
            return todo_id


def process_todo_action(todo_lists: dict, action: str) -> dict:
    """Perform CRUD operations on the todo dictionary."""

    if action == "add":
        print("\n--- Add a New Task ---")
        task_content = input("Enter task content: ").strip()
     
        if not task_content:
            raise InvalidInputError("Todo content cannot be empty.")

        todo_id = generate_todo_id(todo_lists)
        todo_lists[todo_id] = {
            "task_content": task_content,
        }

        save_todo_lists(todo_lists)
        print(f"Task added successfully! ID: {todo_id}")

    elif action == "view":
        if not todo_lists:
            print("\nYour To-Do list is empty.")
        else:
            print(f"\n--- All Tasks ({len(todo_lists)}) ---")
            for todo_id, task_data in todo_lists.items():
                print(f"\nID: {todo_id}")
                print(f"  Content: {task_data['task_content']}")

    elif action == "search":
        query = input("Enter search keyword: ").strip().lower()
        if not query:
            raise InvalidInputError("Search query cannot be empty.")

        found = False
        print("\n--- Search Results ---")
        for todo_id, task_data in todo_lists.items():
            if query in task_data["task_content"].lower():
                print(f"\nID: {todo_id}")
                print(f"  Content: {task_data['task_content']}")
                found = True

        if not found:
            print("No matching tasks found.")

    elif action == "update":
        todo_id = input("Enter the Todo ID to update: ").strip().upper()
        if todo_id not in todo_lists:
            raise TodoListNotFoundError(f"Todo ID '{todo_id}' not found.")

        task_data = todo_lists[todo_id]
        print("\nPress Enter to keep current value.")

        new_content = input(f"Task Content [{task_data['task_content']}]: ").strip()
        if new_content:
            task_data["task_content"] = new_content

        # FIXED: Pass the full todo_lists dictionary instead of just task_data
        save_todo_lists(todo_lists)
        print("Task updated successfully!")

    elif action == "delete":
        todo_id = input("Enter the Todo ID to delete: ").strip().upper()
        if todo_id not in todo_lists:
            raise TodoListNotFoundError(f"Todo ID '{todo_id}' not found.")

        del todo_lists[todo_id]
        save_todo_lists(todo_lists)
        print("Task deleted successfully!")

    return todo_lists


def todo_list_generator() -> None:
    """Run the main To-Do CLI loop."""
    try:
        todo_lists = load_todo_lists()
    except TodoListError as err:
        print(f"Storage Initialization Error: {err}")
        todo_lists = {}

    print("=" * 45)
    print("                 TO-DO CLI")
    print("=" * 45)
    print("Actions:")
    print("  add    -> Add a task")
    print("  view   -> View all tasks")
    print("  search -> Search for a task")
    print("  update -> Update a task")
    print("  delete -> Delete a task")
    print("  exit   -> Exit program")
    print("-" * 45)

    while True:
        try:
            action = input("\nWhat action would you like to perform? > ").strip().lower()

            if not action:
                continue

            if action in ("exit", "quit"):
                print("Exiting To-Do CLI. Goodbye!")
                break

            valid_actions = ("add", "view", "search", "update", "delete")
            if action not in valid_actions:
                raise InvalidInputError(
                    "Invalid action. Choose add, view, search, update, delete, or exit."
                )

            todo_lists = process_todo_action(todo_lists, action)

        except TodoListError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    todo_list_generator()