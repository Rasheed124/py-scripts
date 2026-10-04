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


# Defined character pools
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

    # 1. Guarantee at least one character from each essential category
    guaranteed = [
        secrets.choice(LOWERCASE),
        secrets.choice(UPPERCASE),
        secrets.choice(DIGITS),
        secrets.choice(SYMBOLS),
    ]

    # 2. Fill the remaining slots randomly from the combined pool
    remaining_length = length - len(guaranteed)
    remaining = [secrets.choice(ALL_CHARACTERS) for _ in range(remaining_length)]

    # 3. Combine and shuffle using a cryptographically secure method
    password_list = guaranteed + remaining
    
    # SystemRandom instance for secure shuffling
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