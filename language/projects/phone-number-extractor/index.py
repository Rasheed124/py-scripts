
# import re
# from pathlib import Path


# class EmailExtractorError(Exception):
#     """Base exception class for Email Extractor domain errors."""
#     pass


# class InvalidInputError(EmailExtractorError):
#     """Raised when user selection or text input is invalid."""
#     pass


# class FileAccessError(EmailExtractorError):
#     """Raised when a file cannot be found or read."""
#     pass


# # Standard regex pattern for email address extraction
# PHONE_REGEX = r"(?:0[789]\d{2}[ -]\d{3}[ -]\d{4}|\+234-[789]\d{2}-\d{3}-\d{4})"


# def extract_phone_number(text: str) -> tuple[list[str], int]:
#     """
#     Extracts valid email addresses from text using regular expressions.
#     Returns a tuple containing a list of unique emails and the total count.
#     """
#     if not text.strip():
#         raise InvalidInputError("Provided text is empty.")


#     matches = re.findall(PHONE_REGEX, text)
    
#     unique_emails = list(dict.fromkeys(phone_number for phone_number in matches))

#     return unique_emails, len(unique_emails)


# def extract_phone_number_from_file(file_name: str) -> tuple[list[str], int]:
#     """Reads text from a file and extracts email addresses."""
#     file_path = Path(__file__).parent / file_name

#     try:
#         with open(file_path, "r", encoding="utf-8") as file:
#             content = file.read()
#             return extract_phone_number(content)
#     except FileNotFoundError:
#         raise FileAccessError(f"File '{file_name}' was not found in working directory.")
#     except Exception as e:
#         raise FileAccessError(f"Failed to read file: {e}")


# def run_phone_number_extractor() -> None:
#     """Main CLI loop for the Email Address Extractor."""
#     print("=" * 45)
#     print("        EMAIL ADDRESS EXTRACTOR CLI")
#     print("=" * 45)
#     print("Commands:")
#     print("  'yes' / 'y'   -> Extract emails from file")
#     print("  'no'  / 'n'   -> Enter text directly")
#     print("  'exit'/ 'quit' -> Exit program")
#     print("-" * 45)

#     while True:
#         try:
#             raw_input = input("\nDo you want to extract Phone number from a file? (y/n) > ").strip().lower()

#             if not raw_input:
#                 continue

#             if raw_input in ("exit", "quit"):
#                 print("Exiting Email Extractor. Goodbye!")
#                 break

#             if raw_input in ("no", "n"):
#                 text_content = input("Type your text/sentence:\n > ").strip()
#                 phone_number_list, total_count = extract_phone_number(text_content)

#             elif raw_input in ("yes", "y"):
#                 filename = input("Enter filename (e.g., sample.txt):\n > ").strip()
#                 phone_number_list, total_count = extract_phone_number_from_file(filename)

#             else:
#                 raise InvalidInputError("Please respond with 'yes' (y) or 'no' (n).")

#             print(f"\n--- Results ---")
#             print(f"Total Unique Emails Found: {total_count}")
            
#             if phone_number_list:
#                 for idx, email in enumerate(phone_number_list, start=1):
#                     print(f"  {idx}. {email}")
#             else:
#                 print("No valid email addresses found.")

#         except EmailExtractorError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     run_phone_number_extractor()









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



PHONE_REGEX = r"(?:0[789]\d{2}[ -]\d{3}[ -]\d{4}|\+234-[789]\d{2}-\d{3}-\d{4})"


def normalize_phone_number(raw_phone: str) -> str:
    """
    Normalizes a extracted phone string into standard E.164 international format (+234...).
    Example: '0803-123-4567' -> '+2348031234567'
    """
    # Remove all non-digit characters
    digits = re.sub(r"\D", "", raw_phone)

    if digits.startswith("0") and len(digits) == 11:
        return f"+234{digits[1:]}"
    elif digits.startswith("234") and len(digits) == 13:
        return f"+{digits}"
    
    return f"+{digits}"


def extract_phone_numbers(text: str) -> tuple[list[dict[str, str]], int]:
    """
    Extracts phone numbers from text using regular expressions.
    Returns structured data containing raw strings and normalized E.164 values.
    """
    if not text.strip():
        raise InvalidInputError("Provided text is empty.")

    matches = re.findall(PHONE_REGEX, text)
    
    # Structure data and eliminate duplicate normalized numbers
    seen_normalized = set()
    structured_results = []

    for raw in matches:
        normalized = normalize_phone_number(raw)
        if normalized not in seen_normalized:
            seen_normalized.add(normalized)
            structured_results.append({
                "raw": raw.strip(),
                "normalized": normalized
            })

    return structured_results, len(structured_results)


def extract_phone_numbers_from_file(file_name: str) -> tuple[list[dict[str, str]], int]:
    """Reads text from a file and extracts phone numbers."""
    file_path = Path(__file__).parent / file_name

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return extract_phone_numbers(content)
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

            if raw_input in ("no", "n"):
                text_content = input("Type your text/sentence:\n > ").strip()
                phone_list, total_count = extract_phone_numbers(text_content)

            elif raw_input in ("yes", "y"):
                filename = input("Enter filename (e.g., contacts.txt):\n > ").strip()
                phone_list, total_count = extract_phone_numbers_from_file(filename)

            else:
                raise InvalidInputError("Please respond with 'yes' (y) or 'no' (n).")

            print(f"\n--- Results ---")
            print(f"Total Unique Phone Numbers Found: {total_count}")
            
            if phone_list:
                for idx, item in enumerate(phone_list, start=1):
                    print(f"  {idx}. Normalized: {item['normalized']}  (Raw Match: '{item['raw']}')")
            else:
                print("No valid phone numbers found.")

        except PhoneNumberExtractorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_phone_number_extractor()