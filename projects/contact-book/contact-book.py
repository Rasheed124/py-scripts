

# import random
# import string


# class ContactBookError(Exception):
#     """Base exception for contact book errors."""
#     pass


# class InvalidInputError(ContactBookError):
#     """Raised when user input is invalid."""
#     pass


# def generate_contact_id(contact_book_list):
#     """Generate a unique ID for a contact."""
#     while True:
#         contact_id = "".join(
#             random.choices(
#                 string.ascii_uppercase + string.digits,
#                 k=8,
#             )
#         )

#         if contact_id not in contact_book_list:
#             return contact_id


# def actions_picker_configurator(
#     contact_book_list: dict,
#     action: str = "add",
# ) -> dict:
#     """Perform an action on the existing contact dictionary."""

#     if action == "add":
#         print("\nAdd a new contact")

#         name = input("Name: ").strip()
#         phone_number = input("Phone number: ").strip()
#         email = input("Email: ").strip()

#         if not name:
#             raise InvalidInputError("Name cannot be empty.")

#         generated_contact_id = generate_contact_id(contact_book_list)

#         contact_book_list[generated_contact_id] = {
#             "name": name,
#             "phone_number": phone_number,
#             "email": email,
#         }

#         print(f"Contact added successfully! ID: {generated_contact_id}")

#     elif action == "view":
#         if not contact_book_list:
#             print("\nYour contact book is empty.")
#         else:
#             print("\nAll contacts:")

#             for contact_id, contact in contact_book_list.items():
#                 print(f"\nContact ID: {contact_id}")
#                 print(f"Name: {contact['name']}")
#                 print(f"Phone: {contact['phone_number']}")
#                 print(f"Email: {contact['email']}")

#     elif action == "search":
#         query = input("Enter a name, phone number, or email: ").strip().lower()
#         found = False

#         for contact_id, contact in contact_book_list.items():
#             if any(
#                 query in contact[field].lower()
#                 for field in ("name", "phone_number", "email")
#             ):
#                 print(f"\nContact ID: {contact_id}")
#                 print(f"Name: {contact['name']}")
#                 print(f"Phone: {contact['phone_number']}")
#                 print(f"Email: {contact['email']}")
#                 found = True

#         if not found:
#             print("No matching contact found.")

#     elif action == "update":
#         contact_id = input("Enter the contact ID to update: ").strip().upper()

#         if contact_id not in contact_book_list:
#             print("Contact ID not found.")
#         else:
#             contact = contact_book_list[contact_id]

#             print("Press Enter to keep the current value.")

#             name = input(f"Name [{contact['name']}]: ").strip()
#             phone = input(
#                 f"Phone [{contact['phone_number']}]: "
#             ).strip()
#             email = input(f"Email [{contact['email']}]: ").strip()

#             if name:
#                 contact["name"] = name
#             if phone:
#                 contact["phone_number"] = phone
#             if email:
#                 contact["email"] = email

#             print("Contact updated successfully!")

#     elif action == "delete":
#         contact_id = input("Enter the contact ID to delete: ").strip().upper()

#         if contact_id in contact_book_list:
#             del contact_book_list[contact_id]
#             print("Contact deleted successfully!")
#         else:
#             print("Contact ID not found.")

#     return contact_book_list


# def contact_book_generator() -> None:
#     """Run the main contact book CLI."""

#     # IMPORTANT: Create the dictionary only once, before the loop.
#     contact_book_list = {}

#     print("=" * 45)
#     print(" " * 12 + "CONTACT BOOK")
#     print("=" * 45)
#     print("Actions:")
#     print("  add    -> Add a contact")
#     print("  view   -> View all contacts")
#     print("  search -> Search for a contact")
#     print("  update -> Update a contact")
#     print("  delete -> Delete a contact")
#     print("  exit   -> Exit program")
#     print("-" * 45)

#     while True:
#         try:
#             action = input(
#                 "\nWhat action would you like to perform? > "
#             ).strip().lower()

#             if not action:
#                 continue

#             if action in ("exit", "quit"):
#                 print("Exiting contact book. Goodbye!")
#                 break

#             valid_actions = (
#                 "add",
#                 "view",
#                 "search",
#                 "update",
#                 "delete",
#             )

#             if action not in valid_actions:
#                 raise InvalidInputError(
#                     "Invalid action. Choose add, view, search, "
#                     "update, delete, or exit."
#                 )

#             contact_book_list = actions_picker_configurator(
#                 contact_book_list,
#                 action,
#             )

#         except ContactBookError as err:
#             print(f"Error: {err}")

#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     contact_book_generator()






import json
import random
import string
from pathlib import Path


class ContactBookError(Exception):
    """Base exception for contact book domain errors."""
    pass


class InvalidInputError(ContactBookError):
    """Raised when user input is invalid."""
    pass


class ContactNotFoundError(ContactBookError):
    """Raised when a contact ID does not exist."""
    pass


class StorageError(ContactBookError):
    """Raised when loading or saving JSON data fails."""
    pass


DATA_FILE = Path(__file__).parent / "contacts.json"


def load_contacts() -> dict:
    """Load contacts from JSON storage file if it exists."""
    if not DATA_FILE.exists():
        return {}
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise StorageError(f"Failed to load contacts from storage: {e}")


def save_contacts(contacts: dict) -> None:
    """Save contacts dictionary to JSON storage file."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(contacts, f, indent=4)
    except Exception as e:
        raise StorageError(f"Failed to save contacts to storage: {e}")


def generate_contact_id(contact_book: dict) -> str:
    """Generate a unique 8-character alphanumeric ID for a contact."""
    while True:
        contact_id = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=8)
        )
        if contact_id not in contact_book:
            return contact_id


def process_contact_action(contact_book: dict, action: str) -> dict:
    """Perform CRUD operations on the contact dictionary."""

    if action == "add":
        print("\n--- Add a New Contact ---")
        name = input("Name: ").strip()
        phone_number = input("Phone number: ").strip()
        email = input("Email: ").strip()

        if not name:
            raise InvalidInputError("Contact name cannot be empty.")

        contact_id = generate_contact_id(contact_book)
        contact_book[contact_id] = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
        }

        save_contacts(contact_book)
        print(f"Contact added successfully! ID: {contact_id}")

    elif action == "view":
        if not contact_book:
            print("\nYour contact book is empty.")
        else:
            print(f"\n--- All Contacts ({len(contact_book)}) ---")
            for contact_id, contact in contact_book.items():
                print(f"\nID: {contact_id}")
                print(f"  Name:  {contact['name']}")
                print(f"  Phone: {contact['phone_number']}")
                print(f"  Email: {contact['email']}")

    elif action == "search":
        query = input("Enter search term (name, phone, or email): ").strip().lower()
        if not query:
            raise InvalidInputError("Search query cannot be empty.")

        found = False
        print("\n--- Search Results ---")
        for contact_id, contact in contact_book.items():
            if any(query in contact[field].lower() for field in ("name", "phone_number", "email")):
                print(f"\nID: {contact_id}")
                print(f"  Name:  {contact['name']}")
                print(f"  Phone: {contact['phone_number']}")
                print(f"  Email: {contact['email']}")
                found = True

        if not found:
            print("No matching contacts found.")

    elif action == "update":
        contact_id = input("Enter the Contact ID to update: ").strip().upper()
        if contact_id not in contact_book:
            raise ContactNotFoundError(f"Contact ID '{contact_id}' not found.")

        contact = contact_book[contact_id]
        print("\nPress Enter to keep current values.")

        name = input(f"Name [{contact['name']}]: ").strip()
        phone = input(f"Phone [{contact['phone_number']}]: ").strip()
        email = input(f"Email [{contact['email']}]: ").strip()

        if name:
            contact["name"] = name
        if phone:
            contact["phone_number"] = phone
        if email:
            contact["email"] = email

        save_contacts(contact_book)
        print("Contact updated successfully!")

    elif action == "delete":
        contact_id = input("Enter the Contact ID to delete: ").strip().upper()
        if contact_id not in contact_book:
            raise ContactNotFoundError(f"Contact ID '{contact_id}' not found.")

        del contact_book[contact_id]
        save_contacts(contact_book)
        print("Contact deleted successfully!")

    return contact_book


def contact_book_generator() -> None:
    """Run the main contact book CLI loop."""
    try:
        contact_book = load_contacts()
    except ContactBookError as err:
        print(f"Storage Initialization Error: {err}")
        contact_book = {}

    print("=" * 45)
    print("                 CONTACT BOOK")
    print("=" * 45)
    print("Actions:")
    print("  add    -> Add a contact")
    print("  view   -> View all contacts")
    print("  search -> Search for a contact")
    print("  update -> Update a contact")
    print("  delete -> Delete a contact")
    print("  exit   -> Exit program")
    print("-" * 45)

    while True:
        try:
            action = input("\nWhat action would you like to perform? > ").strip().lower()

            if not action:
                continue

            if action in ("exit", "quit"):
                print("Exiting Contact Book. Goodbye!")
                break

            valid_actions = ("add", "view", "search", "update", "delete")
            if action not in valid_actions:
                raise InvalidInputError(
                    "Invalid action. Choose add, view, search, update, delete, or exit."
                )

            contact_book = process_contact_action(contact_book, action)

        except ContactBookError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    contact_book_generator()