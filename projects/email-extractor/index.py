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
    """
    Analyzes input text and returns frequency distribution along with total count.
    
    Modes:
      'words' / 'w'      -> Returns (word_frequency_dict, total_words)
      'characters' / 'c' -> Returns (char_frequency_dict, total_chars)
    """
    cleaned_mode = sentence.lower().strip()

    return cleaned_mode



  
        # words = [
        #     w.strip(string.punctuation).lower()
        #     for w in raw_words
        #     if w.strip(string.punctuation)
        # ]
        # return dict(Counter(words)), len(words)

    # else:
    #     raise InvalidInputError("Invalid analysis mode. Choose 'words' (w) or 'characters' (c).")



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




def run_word_count_generator() -> None:
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
                print("Exiting counter. Goodbye!")
                break

            if raw_input in ("no", "n"):
                text_content = input("Type your text/sentence:\n > ").strip()
                if not text_content:
                    raise InvalidInputError("Text cannot be empty.")
                
                email = extract_email(text_content)

                print(email)



            elif raw_input in ("yes", "y"):
                filename = input("Enter filename (e.g., sample.txt):\n > ").strip()
                frequency, total_count = analyze_file(filename)

            else:
                raise InvalidInputError("Please respond with 'yes' (y) or 'no' (n).")

            print(f"\n--- Results ---")
            print(f"Total Emails Count is: {total_count}")
            print(f"Frequency Distribution:")
            for item, count in frequency:
                print(f"  '{item}': {count}")

        except WordCountError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_word_count_generator()
