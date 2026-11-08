# import re
# from pathlib import Path
# import string



# class PhoneNumberExtractorError(Exception):
#     """Base exception class for Phone Number Extractor domain errors."""
#     pass


# class InvalidInputError(PhoneNumberExtractorError):
#     """Raised when user selection or text input is invalid."""
#     pass


# class FileAccessError(PhoneNumberExtractorError):
#     """Raised when a file cannot be found or read."""
#     pass


# def extract_word_or_phrase_from_file(word: str) -> dict:
# # def extract_word_or_phrase_from_file(word: str) -> tuple[list[dict[str, str]], int]:
#     """Reads text from a file and extracts phone numbers."""


#     file_path = Path(__file__).parent
#     word_search_chars = [ w.lower().strip(string.punctuation)  for w in word.split() ]


#     try:
#         word_search_result = {}
#         for file in file_path.iterdir():
#             if file.is_file() and file.suffix == ".txt":
#                 file_name = file.name

#                 with open(file, "r", encoding="utf-8") as file:
#                     content = file.read()
#                     file_content_chars = [ w.lower().strip(string.punctuation)  for w in content.split() ]
#                     conttent_search = [ w.lower() for w in word_search_chars if w in file_content_chars]

                    # for word in conttent_search:
                    #      if word in word_search_result:
                    #          word_search_result[word] += 1
                    #      else:
                    #          word_search_result[word] = 1

#         return word_search_result

#     except FileNotFoundError:
#         raise FileAccessError(f"File '{file_name}' was not found in working directory.")
#     except Exception as e:
#         raise FileAccessError(f"Failed to read file: {e}")


# def  text_phrase_in_searcher() -> None:
#     """Main CLI loop for the Phone Number Extractor."""
#     print("=" * 45)
#     print("      PHONE NUMBER EXTRACTOR CLI")
#     print("=" * 45)
#     print("Commands:")
#     print("  'yes' / 'y'   -> Extract phone numbers from file")
#     print("  'no'  / 'n'   -> Enter text directly")
#     print("  'exit'/ 'quit' -> Exit program")
#     print("-" * 45)

#     while True:
#         try:
#             raw_input = input("Type the word or phrase you want to search (y/n) > ").strip().lower()

#             if not raw_input:
#                 continue

#             if  isinstance(raw_input, (int , float)):
#                 raise InvalidInputError('Input can\'t be an integer or float ')


#             if raw_input in ("exit", "quit"):
#                 print("Exiting Phone Number Extractor. Goodbye!")
#                 break

#             word_list = extract_word_or_phrase_from_file(raw_input)

#             print(f"\n--- Results ---")
#             print(f"Ressult for the search word/phrase you typed is : ")            

#             for word, frequency in word_list.items():
#                 print(f"{word} :  {frequency}")


            

#         except PhoneNumberExtractorError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#   text_phrase_in_searcher()















import re
from pathlib import Path


class TextSearcherError(Exception):
    """Base exception class for Text File Searcher domain errors."""
    pass


class InvalidInputError(TextSearcherError):
    """Raised when user search query is invalid."""
    pass


class FileAccessError(TextSearcherError):
    """Raised when directory scanning or file reading fails."""
    pass


def search_text_files(query: str, target_dir: Path | None = None) -> list[dict]:
    """
    Searches all .txt files in target_dir for a given word or phrase.
    Supports case-insensitive exact phrase matching and line-level reporting.
    """

    clean_query = query.strip()

    if not clean_query:
        raise InvalidInputError("Search query cannot be empty.")

    search_path = target_dir if target_dir else Path(__file__).parent

    if not search_path.exists() or not search_path.is_dir():
        raise FileAccessError(f"Search directory '{search_path}' does not exist.")

    results = []
    # Regex pattern matching exact word/phrase with word boundaries where applicable
    query_pattern = re.compile(re.escape(clean_query), re.IGNORECASE)

    try:
        txt_files = list(search_path.glob("*.txt"))
        
        for file_path in txt_files:
            file_matches = []
            
            with open(file_path, "r", encoding="utf-8", errors="ignore") as file_handle:
                for line_num, line in enumerate(file_handle, start=1):
                    matches = list(query_pattern.finditer(line))
                    if matches:
                        file_matches.append({
                            "line_number": line_num,
                            "match_count": len(matches),
                            "line_snippet": line.strip()
                        })

            if file_matches:
                total_occurrences = sum(m["match_count"] for m in file_matches)
                results.append({
                    "filename": file_path.name,
                    "total_count": total_occurrences,
                    "details": file_matches
                })

        return results


    except Exception as e:
        raise FileAccessError(f"Error during directory search: {e}")


def run_text_searcher() -> None:
    """Main CLI loop for Text File Searcher Engine."""
    print("=" * 45)
    print("        TEXT FILE SEARCH ENGINE CLI")
    print("=" * 45)
    print("Commands:")
    print("  Enter any word or phrase to search across .txt files")
    print("  'exit' / 'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("\nSearch Query > ").strip()

            if not raw_input:
                continue

            if raw_input.lower() in ("exit", "quit"):
                print("Exiting Text Searcher. Goodbye!")
                break

            search_results = search_text_files(raw_input)

            # Display Search Results
            print(f"\n--- Search Results for '{raw_input}' ---")
            
            if not search_results:
                print("No matches found across .txt files.")
                continue

            total_file_matches = len(search_results)
            total_occurrences = sum(res["total_count"] for res in search_results)
            print(f"Found {total_occurrences} occurrence(s) across {total_file_matches} file(s):\n")

            for res in search_results:
                print(f"📄 File: {res['filename']} ({res['total_count']} match(es))")
                for match in res["details"]:
                    print(f"   Line {match['line_number']}: {match['line_snippet']}")
                print()

        except TextSearcherError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_text_searcher()