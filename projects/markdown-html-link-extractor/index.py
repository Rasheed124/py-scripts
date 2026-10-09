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


def search_file_markdown(query: str, target_dir: Path | None = None) -> list[dict]:
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
    

    file_name_extracted = Path(clean_query).stem
    print(file_name_extracted)




    # results = []
    # Regex pattern matching exact word/phrase with word boundaries where applicable
    # query_pattern = re.compile(re.escape(clean_query), re.IGNORECASE)

    try:
      print("")

    except Exception as e:
        raise FileAccessError(f"Error during directory search: {e}")

# def search_markdown(query: str, target_dir: Path | None = None) -> list[dict]:
#     """
#     Searches all .txt files in target_dir for a given word or phrase.
#     Supports case-insensitive exact phrase matching and line-level reporting.
#     """

#     clean_query = query.strip()

#     if clean_query in ('f', 'file'):
#         file_name_extracted = Path(clean_query).stem
#         print(file_name_extracted)
#     else: 
#         print("")




#     search_path = target_dir if target_dir else Path(__file__).parent

#     if not search_path.exists() or not search_path.is_dir():
#         raise FileAccessError(f"Search directory '{search_path}' does not exist.")


#     results = []
#     # Regex pattern matching exact word/phrase with word boundaries where applicable
#     query_pattern = re.compile(re.escape(clean_query), re.IGNORECASE)

#     try:
#         txt_files = list(search_path.glob("*.txt"))
        
#         for file_path in txt_files:
#             file_matches = []
            
#             with open(file_path, "r", encoding="utf-8", errors="ignore") as file_handle:
#                 for line_num, line in enumerate(file_handle, start=1):
#                     matches = list(query_pattern.finditer(line))
#                     if matches:
#                         file_matches.append({
#                             "line_number": line_num,
#                             "match_count": len(matches),
#                             "line_snippet": line.strip()
#                         })

#             if file_matches:
#                 total_occurrences = sum(m["match_count"] for m in file_matches)
#                 results.append({
#                     "filename": file_path.name,
#                     "total_count": total_occurrences,
#                     "details": file_matches
#                 })

#         return results


#     except Exception as e:
#         raise FileAccessError(f"Error during directory search: {e}")


def run_text_searcher() -> None:
    """Main CLI loop for Text File Searcher Engine."""
    print("=" * 45)
    print("       MARKDOWN/HTML LINK EXTRACTOR")
    print("=" * 45)
    print("Commands:")
    print("  'file'       -> Extract links from a file")
    print("  'text'       -> Enter text directly")
    print("  'exit'/'quit' -> Exit program")
    print("-" * 45)


    while True:
        try:
            raw_input = input("\nDo you want to extract links from a file or text? (file/text)  > ").strip().lower()

            if not raw_input :
                continue

   
            if raw_input.lower() in ("exit", "quit"):
                print("Exiting Text Searcher. Goodbye!")
                break

                    
            match raw_input:
                case "file" | "f":
                    file_input = input("\nType the name of the file  > ").strip().lower()
                    search_results = search_file_markdown(file_input)
                case "file" | "f" | "text" | "t":
                    texts_input = input("\nType the name of the file  > ").strip().lower()
                    search_results = search_texts_markdown(texts_input)
                case _:
                    raise InvalidInputError("Kindly type between file/text")


     



            # Display Search Results
            print(f"\n--- Search Results for '{raw_input}' ---")
            
            if not search_results:
                print("No matches found across .txt files.")
                continue

            # total_file_matches = len(search_results)
            # total_occurrences = sum(res["total_count"] for res in search_results)
            # print(f"Found {total_occurrences} occurrence(s) across {total_file_matches} file(s):\n")

            # for res in search_results:
            #     print(f"📄 File: {res['filename']} ({res['total_count']} match(es))")
            #     for match in res["details"]:
            #         print(f"   Line {match['line_number']}: {match['line_snippet']}")
            #     print()

        except TextSearcherError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_text_searcher()