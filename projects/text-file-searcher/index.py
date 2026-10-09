import re
from pathlib import Path
import string



class PhoneNumberExtractorError(Exception):
    """Base exception class for Phone Number Extractor domain errors."""
    pass


class InvalidInputError(PhoneNumberExtractorError):
    """Raised when user selection or text input is invalid."""
    pass


class FileAccessError(PhoneNumberExtractorError):
    """Raised when a file cannot be found or read."""
    pass




def extract_word_or_phrase_from_file(word: str) -> dict:
# def extract_word_or_phrase_from_file(word: str) -> tuple[list[dict[str, str]], int]:
    """Reads text from a file and extracts phone numbers."""


    file_path = Path(__file__).parent
    word_search_chars = [ w.lower().strip(string.punctuation)  for w in word.split() ]


    try:
        word_search_result = {}
        for file in file_path.iterdir():
            if file.is_file() and file.suffix == ".txt":
                file_name = file.name

                with open(file, "r", encoding="utf-8") as file:
                    content = file.read()
                    file_content_chars = [ w.lower().strip(string.punctuation)  for w in content.split() ]
                    conttent_search = [ w.lower() for w in word_search_chars if w in file_content_chars]

                    for word in conttent_search:
                         if word in word_search_result:
                             word_search_result[word] += 1
                         else:
                             word_search_result[word] = 1

        return word_search_result

    except FileNotFoundError:
        raise FileAccessError(f"File '{file_name}' was not found in working directory.")
    except Exception as e:
        raise FileAccessError(f"Failed to read file: {e}")


def  text_phrase_in_searcher() -> None:
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
            raw_input = input("Type the word or phrase you want to search (y/n) > ").strip().lower()

            if not raw_input:
                continue

            if  isinstance(raw_input, (int , float)):
                raise InvalidInputError('Input can\'t be an integer or float ')


            if raw_input in ("exit", "quit"):
                print("Exiting Phone Number Extractor. Goodbye!")
                break

            word_list = extract_word_or_phrase_from_file(raw_input)

            print(f"\n--- Results ---")
            print(f"Ressult for the search word/phrase you typed is : ")            

            for word, frequency in word_list.items():
                print(f"{word} :  {frequency}")


            

        except PhoneNumberExtractorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
  text_phrase_in_searcher()