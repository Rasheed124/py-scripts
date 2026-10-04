
# import string
# from pathlib import Path


# class word_countError(Exception):
#     """Base exception class for word_count domain errors."""
#     pass


# class InvalidInputError(word_countError):
#     """Raised when input syntax or parameters are invalid."""
#     pass


# class word_countLengthError(word_countError):
#     """Raised when the requested word_count length is too short."""
#     pass



# def word_frequency_list_generator(new_character):
#     character_frequency = {}
#     for charcter in new_character:
#         if charcter not in character_frequency:
#             character_frequency[charcter] = 1
#         else:
#             character_frequency[charcter] += 1
#     return character_frequency

# def  generate_word_count(characters: string) -> tuple:

#     new_word_list = []
#     splitted_word = characters.split()

#     for word in splitted_word:
#         formatted_word = ""

#         for char in word:
#             if char not in string.punctuation:
#                 formatted_word += char

#         new_word_list.append(formatted_word)

#     word_count = len(new_word_list)

#     word_frequency =  word_frequency_list_generator(new_word_list)

#     return word_frequency, word_count


# def generate_character_count(characters: string) -> tuple:
#     new_character = ""
#     character_count =  0

#     # character count
#     for charac in characters.replace(' ', ""):
#         if charac not in string.punctuation:
#             new_character += charac
#             character_count =  len(new_character)


#     character_frequency =  word_frequency_list_generator(new_character)

#     return character_frequency, character_count


# def all_count(characters: str, choosen_terms: str) -> tuple:
#     """
#     Generates a cryptographically secure random word_count.
#     Guarantees inclusion of lowercase, uppercase, digit, and symbol characters.
#     """

#     if choosen_terms.lower() in ('characters', 'character', 'c'):
#         # Character Count
#         result = generate_character_count(characters)
#         return result[0], result[1]

#     elif choosen_terms.lower() in ('words', 'word', 'w'):
#         # Word Count
#         result = generate_word_count(characters)
#         return result[0], result[1]

        
#     else:
#         raise InvalidInputError("None of your choice matches, try again")

    
# def generate_word_count_from_file(file_name: str, choosen_terms: str) -> tuple:
#     """
#     Generates a cryptographically secure random word_count.
#     Guarantees inclusion of lowercase, uppercase, digit, and symbol characters.
#     """

#     file_path = Path(__file__).parent / file_name

#     try:
#         with open(file_path, "r") as file:
#             content = file.read()

#             if choosen_terms.lower() in ('characters', 'character', 'c'):
#                 # Character Count
#                 result = generate_character_count(characters=content)
#                 return result[0], result[1]

#             elif choosen_terms.lower() in ('words', 'word', 'w'):
#                 # Word Count
#                 result = generate_word_count(characters=content)
#                 return result[0], result[1]

                
#             else:
#                 raise InvalidInputError("None of your choice matches, try again")
            

#     except FileNotFoundError:
#         raise FileNotFoundError(f"File not found: {file_name}")


# def run_word_count_generator() -> None:
#     """Main CLI loop for the word_count Generator."""
#     print("=" * 45)
#     print("       WORD / CHARACTER COUNTER")
#     print("=" * 45)
#     print("Commands:")
#     print("  'file'   -> Count text from a file")
#     print("  'text'   -> Type text directly")
#     print("  'exit' / 'quit' -> Exit program")
#     print("-" * 45)
#     while True:
#         try:
#             raw_input = input("Do you want to count text from a file? Answer yes or no > ").strip()

#             if not raw_input:
#                 continue

#             if raw_input.lower() in ("no", "n"):
#                 user_input_text = input("Type your text/sentence: \n > ").strip()
#                 user_input_word_or_character = input("Do you wish to count between each word or character: \n > ").strip()

               

#                 word_count_result = all_count(user_input_text, user_input_word_or_character)
#                 result = word_count_result


#                 print(f"Total characters: {result[1]}")
#                 print("Word frequency:")

#                 for key, value in result[0].items():
#                     print(f"{key}: {value}")


#             if raw_input.lower() in ("yes", "y"):
#                 user_input_tex = input("Enter filename: \n > ").strip()
#                 user_input_word_or_character = input("Do you wish to count between each word or character: \n > ").strip()

#                 word__file_count_result = generate_word_count_from_file(user_input_tex, user_input_word_or_character) 

#                 result = word__file_count_result
        
        
#                 print(f"Total characters: {result[1]}")
#                 print("Word frequency:")

#                 for key, value in result[0].items():
#                     print(f"{key}: {value}")
        


#             if raw_input.lower() in ("exit", "quit"):
#                 print("Exiting word_count generator. Goodbye!")
#                 break

      

#         except word_countError as err:
#             print(f"Error: {err}\n")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     run_word_count_generator()







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


def analyze_text(text: str, mode: str) -> tuple[dict[str, int], int]:
    """
    Analyzes input text and returns frequency distribution along with total count.
    
    Modes:
      'words' / 'w'      -> Returns (word_frequency_dict, total_words)
      'characters' / 'c' -> Returns (char_frequency_dict, total_chars)
    """
    cleaned_mode = mode.lower().strip()

    if cleaned_mode in ("words", "word", "w"):
        raw_words = text.split()
        words = [
            w.strip(string.punctuation).lower()
            for w in raw_words
            if w.strip(string.punctuation)
        ]
        return dict(Counter(words)), len(words)

    elif cleaned_mode in ("characters", "character", "c"):
        chars = [
            c.lower()
            for c in text
            if c not in string.punctuation and not c.isspace()
        ]
        return dict(Counter(chars)), len(chars)

    else:
        raise InvalidInputError("Invalid analysis mode. Choose 'words' (w) or 'characters' (c).")


def analyze_file(file_name: str, mode: str) -> tuple[dict[str, int], int]:
    """Reads text from a file and delegates analysis to analyze_text()."""
    file_path = Path(__file__).parent / file_name

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return analyze_text(content, mode)
    except FileNotFoundError:
        raise FileAccessError(f"File '{file_name}' was not found in working directory.")
    except Exception as e:
        raise FileAccessError(f"Failed to read file: {e}")


def run_word_count_generator() -> None:
    """Main CLI loop for the Word/Character Counter."""
    print("=" * 45)
    print("        WORD & CHARACTER COUNTER ENGINE")
    print("=" * 45)
    print("Commands:")
    print("  'yes' / 'y' -> Read from file")
    print("  'no'  / 'n' -> Type text directly")
    print("  'exit'/ 'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("\nDo you want to count text from a file? (y/n) > ").strip().lower()

            if not raw_input:
                continue

            if raw_input in ("exit", "quit"):
                print("Exiting counter. Goodbye!")
                break

            if raw_input in ("no", "n"):
                text_content = input("Type your text/sentence:\n > ").strip()
                if not text_content:
                    raise InvalidInputError("Text cannot be empty.")
                
                mode = input("Count 'words' (w) or 'characters' (c):\n > ").strip()
                frequency, total_count = analyze_text(text_content, mode)

            elif raw_input in ("yes", "y"):
                filename = input("Enter filename (e.g., sample.txt):\n > ").strip()
                mode = input("Count 'words' (w) or 'characters' (c):\n > ").strip()
                frequency, total_count = analyze_file(filename, mode)

            else:
                raise InvalidInputError("Please respond with 'yes' (y) or 'no' (n).")

            unit_label = "words" if mode.lower() in ("words", "word", "w") else "characters"
            print(f"\n--- Results ---")
            print(f"Total {unit_label}: {total_count}")
            print(f"Frequency Distribution:")
            for item, count in sorted(frequency.items(), key=lambda x: x[1], reverse=False):
                print(f"  '{item}': {count}")

        except WordCountError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_word_count_generator()
