# import json
# import random
# import string
# from pathlib import Path


# class ExpenseListTrackerError(Exception):
#     """Base exception for To-Do CLI domain errors."""
#     pass


# class InvalidInputError(ExpenseListTrackerError):
#     """Raised when user input is invalid."""
#     pass

# class ExpenseNotFoundError(ExpenseListTrackerError):
#     """Raised when a Todo ID does not exist."""
#     pass


# class StorageError(ExpenseListTrackerError):
#     """Raised when loading or saving JSON data fails."""
#     pass


# DATA_FILE = Path(__file__).parent / "expense_lists.json"


# def load_expense_lists() -> dict:
#     """Load todo lists from JSON storage file if it exists."""
#     if not DATA_FILE.exists():
#         return {}
#     try:
#         with open(DATA_FILE, "r", encoding="utf-8") as f:
#             return json.load(f)
#     except Exception as e:
#         raise StorageError(f"Failed to load todo lists from storage: {e}")


# def save_expense_lists(content: dict) -> None:
#     """Save content dictionary to JSON storage file."""
#     try:
#         with open(DATA_FILE, "w", encoding="utf-8") as f:
#             json.dump(content, f, indent=4)
#     except Exception as e:
#         raise StorageError(f"Failed to save todo lists to storage: {e}")


# def generate_expense_id(todo_lists: dict) -> str:
#     """Generate a unique 8-character alphanumeric ID for a task."""
#     while True:
#         todo_id = "".join(
#             random.choices(string.ascii_uppercase + string.digits, k=8)
#         )
#         if todo_id not in todo_lists:
#             return todo_id


# def process_expense_action(expense_lists: dict, action: str) -> dict:
#     """Perform CRUD operations on the expense dictionary."""

#     if action == "add":
#         print("\n--- Record a New Expense ---")

#         expense_name = input("Enter expense name: ").strip()
#         expense_amount = input("Enter amount: ").strip()
#         expense_category = input("Enter category: ").strip()
#         expense_date = input("Enter date (YYYY-MM-DD): ").strip()

#         if not expense_name:
#             raise InvalidInputError("Expense name cannot be empty.")

#         expense_id = generate_expense_id(expense_lists)
#         expense_lists[expense_id] = {
#             "expense_name": expense_name,
#             "expense_amount": expense_amount,
#             "expense_category": expense_category,
#             "expense_date": expense_date,
#         }

#         save_expense_lists(expense_lists)
#         print(f"Expense recorded successfully! ID: {expense_id}")

#     elif action == "view":
#         if not expense_lists:
#             print("\nYour expense list is empty.")
#         else:
#             print(f"\n--- All Expenses ({len(expense_lists)}) ---")
#             for expense_id, expense_data in expense_lists.items():
#                 print(f"\nID: {expense_id}")
#                 print(f"  Name: {expense_data['expense_name']}")
#                 print(f"  Amount: {expense_data['expense_amount']}")
#                 print(f"  Category: {expense_data['expense_category']}")
#                 print(f"  Date: {expense_data['expense_date']}")

#     elif action == "search":
#         query = input("Enter search keyword: ").strip().lower()
#         query = "expense name".split()
#         query = "_".join(query)

#         if not query:
#             raise InvalidInputError("Search query cannot be empty.")

#         found = False
#         print("\n--- Search Results ---")
#         for expense_id, expense_data in expense_lists.items():
#             if any(query in str(expense_data[field]).lower() for field in
#                 ("expense_name", "expense_amount", "expense_category", "expense_date")):
#                 print(f"\nID: {expense_id}")
#                 print(f"  Name: {expense_data['expense_name']}")
#                 print(f"  Amount: {expense_data['expense_amount']}")
#                 print(f"  Category: {expense_data['expense_category']}")
#                 print(f"  Date: {expense_data['expense_date']}")
#                 found = True

#         if not found:
#             print("No matching expenses found.")

#     elif action == "update":
#         expense_id = input("Enter the Expense ID to update: ").strip().upper()
#         if expense_id not in expense_lists:
#             raise ExpenseNotFoundError(f"Expense ID '{expense_id}' not found.")

#         expense_data = expense_lists[expense_id]
#         print("\nPress Enter to keep current value.")

#         new_name = input(f"Expense Name [{expense_data['expense_name']}]: ").strip()
#         new_amount = input(f"Amount [{expense_data['expense_amount']}]: ").strip()
#         new_category = input(f"Category [{expense_data['expense_category']}]: ").strip()
#         new_date = input(f"Date [{expense_data['expense_date']}]: ").strip()

#         if new_name:
#             expense_data["expense_name"] = new_name
#         if new_amount:
#             expense_data["expense_amount"] = new_amount
#         if new_category:
#             expense_data["expense_category"] = new_category
#         if new_date:
#             expense_data["expense_date"] = new_date

#         save_expense_lists(expense_lists)
#         print("Expense updated successfully!")

#     elif action == "delete":
#         expense_id = input("Enter the Expense ID to delete: ").strip().upper()
#         if expense_id not in expense_lists:
#             raise ExpenseNotFoundError(f"Expense ID '{expense_id}' not found.")

#         del expense_lists[expense_id]
#         save_expense_lists(expense_lists)
#         print("Expense deleted successfully!")

#     elif action == "summary":


#         print("=" * 10 + " EXPENSE TRACKER SUMMARY " + "=" * 10)
#         expense_amounts = [ int(expense_data['expense_amount']) for _, expense_data in expense_lists.items() ]
#         total_expense_amount =  sum(expense_amounts)

#         print(f"Total Expenses: {len(expense_lists)}")
#         print(f"Total Amount Spent:  ₦{total_expense_amount}")

#         print("Expenses by Category:")
#         for expense_id, expense_data in expense_lists.items():
#             print(f"   {expense_data['expense_category']}: {expense_data['expense_amount']}")
        
#         print("=" * 20)
        

#     return expense_lists


# def todo_list_generator() -> None:
#     """Run the main To-Do CLI loop."""
#     try:
#         expense_lists = load_expense_lists()
#     except ExpenseListTrackerError as err:
#         print(f"Storage Initialization Error: {err}")
#         expense_lists = {}
#     print("=" * 45)
#     print("              EXPENSE TRACKER")
#     print("=" * 45)
#     print("Actions:")
#     print("  add     -> Record an expense")
#     print("  view    -> View all expenses")
#     print("  summary -> View spending summary")
#     print("  search  -> Search expenses")
#     print("  delete  -> Delete an expense")
#     print("  exit    -> Exit program")
#     print("-" * 45)

#     while True:
#         try:
#             action = input("\nWhat action would you like to perform? > ").strip().lower()

#             if not action:
#                 continue

#             if action in ("exit", "quit"):
#                 print("Exiting To-Do CLI. Goodbye!")
#                 break

#             valid_actions = ("add", "view", "summary", "search", "delete")

#             if action not in valid_actions:
#                 raise InvalidInputError(
#                     "Invalid action. Choose add, view, summary, update, delete, or exit."
#                 )

#             expense_lists = process_expense_action(expense_lists, action)

#         except ExpenseListTrackerError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     todo_list_generator()



















import json
import random
import string
from pathlib import Path


class ExpenseTrackerError(Exception):
    """Base exception for Expense Tracker domain errors."""
    pass


class InvalidInputError(ExpenseTrackerError):
    """Raised when user input is invalid."""
    pass


class ExpenseNotFoundError(ExpenseTrackerError):
    """Raised when an Expense ID does not exist."""
    pass


class StorageError(ExpenseTrackerError):
    """Raised when loading or saving JSON data fails."""
    pass


DATA_FILE = Path(__file__).parent / "expenses.json"


def load_expenses() -> dict:
    """Load expenses from JSON storage file if it exists."""
    if not DATA_FILE.exists():
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise StorageError(f"Failed to load expenses from storage: {e}")


def save_expenses(content: dict) -> None:
    """Save content dictionary to JSON storage file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4)
    except Exception as e:
        raise StorageError(f"Failed to save expenses to storage: {e}")


def generate_expense_id(expenses: dict) -> str:
    """Generate a unique 8-character alphanumeric ID for an expense."""
    while True:
        expense_id = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=8)
        )
        if expense_id not in expenses:
            return expense_id


def process_expense_action(expenses: dict, action: str) -> dict:
    """Perform CRUD and aggregation operations on the expense dictionary."""

    if action == "add":
        print("\n--- Record a New Expense ---")
        expense_name = input("Enter expense name: ").strip()
        
        amount_str = input("Enter amount (e.g., 1500.50): ").strip()
        try:
            expense_amount = float(amount_str)
            if expense_amount < 0:
                raise ValueError("Amount cannot be negative.")
        except ValueError:
            raise InvalidInputError("Invalid amount format. Please enter a valid number.")

        expense_category = input("Enter category (e.g., Food, Transport): ").strip()
        expense_date = input("Enter date (YYYY-MM-DD): ").strip()

        if not expense_name:
            raise InvalidInputError("Expense name cannot be empty.")
        if not expense_category:
            raise InvalidInputError("Category cannot be empty.")

        expense_id = generate_expense_id(expenses)
        expenses[expense_id] = {
            "expense_name": expense_name,
            "expense_amount": expense_amount,
            "expense_category": expense_category,
            "expense_date": expense_date,
        }

        save_expenses(expenses)
        print(f"Expense recorded successfully! ID: {expense_id}")

    elif action == "view":
        if not expenses:
            print("\nYour expense list is empty.")
        else:
            print(f"\n--- All Expenses ({len(expenses)}) ---")
            for expense_id, data in expenses.items():
                print(f"\nID: {expense_id}")
                print(f"  Name:     {data['expense_name']}")
                print(f"  Amount:   ₦{data['expense_amount']:,.2f}")
                print(f"  Category: {data['expense_category']}")
                print(f"  Date:     {data['expense_date']}")

    elif action == "search":
        query = input("Enter search keyword (name, category, or date): ").strip().lower()
        if not query:
            raise InvalidInputError("Search query cannot be empty.")

        found = False
        print("\n--- Search Results ---")
        for expense_id, data in expenses.items():
            if any(query in str(data[field]).lower() for field in ("expense_name", "expense_category", "expense_date", "expense_amount")):
                print(f"\nID: {expense_id}")
                print(f"  Name:     {data['expense_name']}")
                print(f"  Amount:   ₦{data['expense_amount']:,.2f}")
                print(f"  Category: {data['expense_category']}")
                print(f"  Date:     {data['expense_date']}")
                found = True

        if not found:
            print("No matching expenses found.")

    elif action == "update":
        expense_id = input("Enter the Expense ID to update: ").strip().upper()
        if expense_id not in expenses:
            raise ExpenseNotFoundError(f"Expense ID '{expense_id}' not found.")

        data = expenses[expense_id]
        print("\nPress Enter to keep current value.")

        new_name = input(f"Expense Name [{data['expense_name']}]: ").strip()
        new_amount_str = input(f"Amount [{data['expense_amount']}]: ").strip()
        new_category = input(f"Category [{data['expense_category']}]: ").strip()
        new_date = input(f"Date [{data['expense_date']}]: ").strip()

        if new_name:
            data["expense_name"] = new_name
        if new_amount_str:
            try:
                data["expense_amount"] = float(new_amount_str)
            except ValueError:
                raise InvalidInputError("Invalid amount format. Update aborted for amount.")
        if new_category:
            data["expense_category"] = new_category
        if new_date:
            data["expense_date"] = new_date

        save_expenses(expenses)
        print("Expense updated successfully!")

    elif action == "delete":
        expense_id = input("Enter the Expense ID to delete: ").strip().upper()
        if expense_id not in expenses:
            raise ExpenseNotFoundError(f"Expense ID '{expense_id}' not found.")

        del expenses[expense_id]
        save_expenses(expenses)
        print("Expense deleted successfully!")

    elif action == "summary":
        if not expenses:
            print("\nYour expense list is empty.")
            return expenses

        print("\n" + "=" * 10 + " EXPENSE TRACKER SUMMARY " + "=" * 10)
        
        total_amount = sum(float(data['expense_amount']) for data in expenses.values())
        print(f"Total Recorded Expenses: {len(expenses)}")
        print(f"Total Amount Spent:      ₦{total_amount:,.2f}")

        category_totals = {}
        for data in expenses.values():
            cat = data['expense_category'].title()
            category_totals[cat] = category_totals.get(cat, 0.0) + float( data['expense_amount'])

        print("\nTotals by Category:")
        for category, cat_total in category_totals.items():
            print(f"  • {category}: ₦{cat_total:,.2f}")

        print("=" * 45)

    return expenses


def expense_tracker_generator() -> None:
    """Run the main Expense Tracker CLI loop."""
    try:
        expenses = load_expenses()
    except ExpenseTrackerError as err:
        print(f"Storage Initialization Error: {err}")
        expenses = {}

    print("=" * 45)
    print("                 EXPENSE TRACKER")
    print("=" * 45)
    print("Actions:")
    print("  add     -> Record an expense")
    print("  view    -> View all expenses")
    print("  summary -> View spending summary")
    print("  search  -> Search expenses")
    print("  update  -> Update an expense")
    print("  delete  -> Delete an expense")
    print("  exit    -> Exit program")
    print("-" * 45)

    while True:
        try:
            action = input("\nWhat action would you like to perform? > ").strip().lower()

            if not action:
                continue

            if action in ("exit", "quit"):
                print("Exiting Expense Tracker. Goodbye!")
                break

            valid_actions = ("add", "view", "summary", "search", "update", "delete")

            if action not in valid_actions:
                raise InvalidInputError(
                    "Invalid action. Choose add, view, summary, search, update, delete, or exit."
                )

            expenses = process_expense_action(expenses, action)

        except ExpenseTrackerError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    expense_tracker_generator()