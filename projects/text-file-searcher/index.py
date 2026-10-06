import re
from pathlib import Path


class PhoneNumberExtractorError(Exception):
    """Base exception class for Phone Number Extractor domain errors."""
    pass


class InvalidInputError(PhoneNumberExtractorError):
    """Raised when user selection or text input is invalid."""
    pass


class FileAccessError(PhoneNumberExtractorError):
    """Raised when a file cannot be found or read."""
    pass




def extract_word_or_phrase_from_file(file_name: str) -> tuple[list[dict[str, str]], int]:
    """Reads text from a file and extracts phone numbers."""
    file_path = Path(__file__).parent / file_name

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            # return extract_word_or_phrase(content)
    except FileNotFoundError:
        raise FileAccessError(f"File '{file_name}' was not found in working directory.")
    except Exception as e:
        raise FileAccessError(f"Failed to read file: {e}")


def run_phone_number_extractor() -> None:
    """Main CLI loop for the Phone Number Extractor."""
    print("=" * 45)
    print("      PHONE NUMBER EXTRACTOR CLI")
    print("=" * 45)
    print("Commands:")
    print("  'yes' / 'y'   -> Extract phone numbers from file")
    print("  'no'  / 'n'   -> Enter text directly")
    print("  'exit'/ 'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("\nDo you want to extract Phone numbers from a file? (y/n) > ").strip().lower()

            if not raw_input:
                continue

            if raw_input in ("exit", "quit"):
                print("Exiting Phone Number Extractor. Goodbye!")
                break

          

            print(f"\n--- Results ---")
            print(f"Total Unique Phone Numbers Found: ")
            
           

        except PhoneNumberExtractorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_phone_number_extractor()