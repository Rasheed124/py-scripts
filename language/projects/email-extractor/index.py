import string
from collections import Counter
from pathlib import Path


class WordCountError(Exception):
    """Base exception class for Word Counter domain errors."""
    pass


class InvalidInputError(WordCountError):
    """Raised when user selection or text input is invalid."""
    pass


class FileAccessError(WordCountError):
    """Raised when a file cannot be found or read."""
    pass


def extract_email(sentence: str) -> tuple[dict[str, int], int]:
   
    cleaned_sentence = sentence.lower().strip()

    sentence_split =  cleaned_sentence.split()

    word_joined = []
    for word in sentence_split:
        if "@" in word and "." in word:
            word_joined.append(word.strip(string.punctuation))
    return word_joined, len(word_joined)




def analyze_file(file_name: str) -> tuple[dict[str, int], int]:
    """Reads text from a file and delegates analysis to analyze_sentence()."""
    file_path = Path(__file__).parent / file_name

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return extract_email(content)
    except FileNotFoundError:
        raise FileAccessError(f"File '{file_name}' was not found in working directory.")
    except Exception as e:
        raise FileAccessError(f"Failed to read file: {e}")




def run_email_extractor() -> None:
    """Main CLI loop for the Email Address Extractor."""
    print("=" * 45)
    print("         EMAIL ADDRESS EXTRACTOR")
    print("=" * 45)
    print("Commands:")
    print("  'yes' / 'y' -> Extract emails from file")
    print("  'no'  / 'n' -> Enter text directly")
    print("  'exit'/ 'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("\nDo you want to extract emails from a file? (y/n) > ").strip().lower()

            if not raw_input:
                continue

            if raw_input in ("exit", "quit"):
                print("Exiting Email extractor. Goodbye!")
                break

            if raw_input in ("no", "n"):
                text_content = input("Type your text/sentence:\n > ").strip()
                if not text_content:
                    raise InvalidInputError("Text cannot be empty.")
                
                email_list, total_count = extract_email(text_content)

            
            elif raw_input in ("yes", "y"):
                filename = input("Enter filename (e.g., sample.txt):\n > ").strip()
                email_list, total_count = analyze_file(filename)


            else:
                raise InvalidInputError("Please respond with 'yes' (y) or 'no' (n).")

            print(f"Total Emails Count is: {total_count}")
            for key, email in enumerate(email_list, start=1):
                print(f"  '{key}': {email}")

        except WordCountError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_email_extractor()














# ============================================= AFTER AI REVIEW







import re
from pathlib import Path


class EmailExtractorError(Exception):
    """Base exception class for Email Extractor domain errors."""
    pass


class InvalidInputError(EmailExtractorError):
    """Raised when user selection or text input is invalid."""
    pass


class FileAccessError(EmailExtractorError):
    """Raised when a file cannot be found or read."""
    pass


EMAIL_REGEX = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails(text: str) -> tuple[list[str], int]:
    """
    Extracts valid email addresses from text using regular expressions.
    Returns a tuple containing a list of unique emails and the total count.
    """
    if not text.strip():
        raise InvalidInputError("Provided text is empty.")

    matches = re.findall(EMAIL_REGEX, text)
    
    unique_emails = list(dict.fromkeys(email.lower() for email in matches))

    return unique_emails, len(unique_emails)


def extract_emails_from_file(file_name: str) -> tuple[list[str], int]:
    """Reads text from a file and extracts email addresses."""
    file_path = Path(__file__).parent / file_name

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return extract_emails(content)
    except FileNotFoundError:
        raise FileAccessError(f"File '{file_name}' was not found in working directory.")
    except Exception as e:
        raise FileAccessError(f"Failed to read file: {e}")


def run_email_extractor() -> None:
    """Main CLI loop for the Email Address Extractor."""
    print("=" * 45)
    print("        EMAIL ADDRESS EXTRACTOR CLI")
    print("=" * 45)
    print("Commands:")
    print("  'yes' / 'y'   -> Extract emails from file")
    print("  'no'  / 'n'   -> Enter text directly")
    print("  'exit'/ 'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("\nDo you want to extract emails from a file? (y/n) > ").strip().lower()

            if not raw_input:
                continue

            if raw_input in ("exit", "quit"):
                print("Exiting Email Extractor. Goodbye!")
                break

            if raw_input in ("no", "n"):
                text_content = input("Type your text/sentence:\n > ").strip()
                email_list, total_count = extract_emails(text_content)

            elif raw_input in ("yes", "y"):
                filename = input("Enter filename (e.g., sample.txt):\n > ").strip()
                email_list, total_count = extract_emails_from_file(filename)

            else:
                raise InvalidInputError("Please respond with 'yes' (y) or 'no' (n).")

            print(f"\n--- Results ---")
            print(f"Total Unique Emails Found: {total_count}")
            
            if email_list:
                for idx, email in enumerate(email_list, start=1):
                    print(f"  {idx}. {email}")
            else:
                print("No valid email addresses found.")

        except EmailExtractorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_email_extractor()
