# import string
# import random

# string.ascii_lowercase
# string.ascii_uppercase


# class PasswordError(Exception):
#     """Base exception class for Password domain errors."""
#     pass


# class InvalidInputError(PasswordError):
#     """Raised when input syntax or characters are invalid."""
#     pass


# class InvalidPasswordError(PasswordError):
#     """Raised when runtime math evaluation fails."""
#     pass



# password_characters = (
#     {str(i) for i in range(10)}
#     | set(string.ascii_letters)
#     | set("!@#$%^&*")
# )



# def generate_password():

#     while True:
#         try:
#             user_input = input("Type the length of characters you want: ").strip().replace(" ", "")

#             if not user_input:
#                 continue

#             if not user_input.isdigit():
#                 print("Input contains only numbers")
#                 continue

#             if not user_input:
#                 print("Input can only contain didgit numbers not string type")
#                 continue

#             length_digit = int(user_input)
#             password_characters_string = ""
#             for chars in password_characters:
#                 password_characters_string += chars

#             random_nums = "".join(random.choices(password_characters_string, k=length_digit ))

#             print(random_nums)
#         except PasswordError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break



# if __name__ == "__main__":  
#     generate_password()








##################################################   AFTER REVIEW ########################################################



import secrets
import string


class PasswordError(Exception):
    """Base exception class for Password domain errors."""
    pass


class InvalidInputError(PasswordError):
    """Raised when input syntax or parameters are invalid."""
    pass


class PasswordLengthError(PasswordError):
    """Raised when the requested password length is too short."""
    pass


LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*"

ALL_CHARACTERS = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS


def generate_secure_password(length: int) -> str:
    """
    Generates a cryptographically secure random password.
    Guarantees inclusion of lowercase, uppercase, digit, and symbol characters.
    """
    if length < 8:
        raise PasswordLengthError("Password length must be at least 8 characters for security.")

    guaranteed = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]

    remaining_length = length - len(guaranteed)
    remaining = [secrets.choice(ALL_CHARACTERS) for _ in range(remaining_length)]

    password_list = guaranteed + remaining
    
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)


def run_password_generator() -> None:
    """Main CLI loop for the Password Generator."""
    print("=" * 45)
    print("     CRYPTOGRAPHIC PASSWORD GENERATOR")
    print("=" * 45)
    print("Commands:")
    print("  Enter length (e.g., 12, 16, 32)")
    print("  'exit' / 'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("password len > ").strip()

            if not raw_input:
                continue

            if raw_input.lower() in ("exit", "quit"):
                print("Exiting password generator. Goodbye!")
                break

            if not raw_input.isdigit():
                raise InvalidInputError("Length must be a positive integer.")

            length = int(raw_input)
            password = generate_secure_password(length)

            print(f"Generated Password: {password}\n")

        except PasswordError as err:
            print(f"Error: {err}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_password_generator()