


import string


class word_countError(Exception):
    """Base exception class for word_count domain errors."""
    pass


class InvalidInputError(word_countError):
    """Raised when input syntax or parameters are invalid."""
    pass


class word_countLengthError(word_countError):
    """Raised when the requested word_count length is too short."""
    pass





def generate_word_count(characters: str) -> tuple:
    """
    Generates a cryptographically secure random word_count.
    Guarantees inclusion of lowercase, uppercase, digit, and symbol characters.
    """

    original_character =  characters
    new_character = ""
    character_count =  0


    # character count
    for charac in characters.replace(' ', ""):
        if charac not in string.punctuation:
            new_character += charac
            character_count =  len(new_character)


    # Word Count
    new_word_list = []
    splitted_word = characters.split()

    for word in splitted_word:
        formatted_word = ""

        for char in word:
            if char not in string.punctuation:
                formatted_word += char

        new_word_list.append(formatted_word)

    word_count = len(new_word_list)
        
    

    return new_word_list, word_count

def generate_word_count_from_file(characters: str) -> tuple:
    """
    Generates a cryptographically secure random word_count.
    Guarantees inclusion of lowercase, uppercase, digit, and symbol characters.
    """

    original_character =  characters

    return original_character, 4
  


def run_word_count_generator() -> None:
    """Main CLI loop for the word_count Generator."""
    print("=" * 45)
    print("       WORD / CHARACTER COUNTER")
    print("=" * 45)
    print("Commands:")
    print("  'file'   -> Count text from a file")
    print("  'text'   -> Type text directly")
    print("  'exit' / 'quit' -> Exit program")
    print("-" * 45)
    while True:
        try:
            raw_input = input("Do you want to count text from a file? > ").strip()

            if not raw_input:
                continue

            if raw_input.lower() in ("no", "n"):
                user_input_tex = input("Type your text/sentence: \n > ").strip()
                word_count_result = generate_word_count(user_input_tex) 
                print(word_count_result)


            if raw_input.lower() in ("yes", "y"):
                user_input_tex = input("Enter filename: \n > ").strip()
                word__file_count_result = generate_word_count_from_file(user_input_tex) 
                print(word__file_count_result)
                



            if raw_input.lower() in ("exit", "quit"):
                print("Exiting word_count generator. Goodbye!")
                break

            # if not raw_input.isdigit():
            #     raise InvalidInputError("Length must be a positive integer.")

            # length = int(raw_input)
            # word_count = generate_secure_word_count(length)

            # print(f"Generated word_count: {word_count}\n")

        except word_countError as err:
            print(f"Error: {err}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_word_count_generator()