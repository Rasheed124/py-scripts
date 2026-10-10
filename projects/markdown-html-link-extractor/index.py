# import re
# from pathlib import Path


# class TextSearcherError(Exception):
#     """Base exception class for Text File Searcher domain errors."""
#     pass


# class InvalidInputError(TextSearcherError):
#     """Raised when user search query is invalid."""
#     pass


# class FileAccessError(TextSearcherError):
#     """Raised when directory scanning or file reading fails."""
#     pass


# def search_file_markdown(query: str, target_dir: Path | None = None) -> dict:
#     """
#     Searches all .txt files in target_dir for a given word or phrase.
#     Supports case-insensitive exact phrase matching and line-level reporting.
#     """

#     clean_query = query.strip()

#     if not clean_query:
#         raise InvalidInputError("Search query cannot be empty.")

#     extracted_file_name = Path(clean_query).stem

#     search_path = target_dir if target_dir else Path(__file__).parent

#     if not search_path.exists() or not search_path.is_dir():
#         raise FileAccessError(f"Search directory '{search_path}' does not exist.")

#     allowed_extensions = (".md", ".html", ".htm", ".txt")

#     text_files = [
#         file
#         for extension in allowed_extensions
#         for file in search_path.glob(f"*{extension}")
#     ]

#     original_file_path = ""
#     for file in text_files:
#         if file.stem == extracted_file_name:
#             original_file_path = file

#     if not original_file_path:
#         raise FileAccessError("No supported files found.")

        
#     try:
      
#         query_pattern = re.compile(re.escape("http"), re.IGNORECASE)
#         file_matches = []
#         result = {}

#         with open(original_file_path, "r", encoding="utf-8", errors="ignore") as file_handle:
#             for line_num, line in enumerate(file_handle, start=1):

#                 matches = list(query_pattern.finditer(line))
#                 if matches:
#                     file_matches.append({
#                         "line_number": line_num,
#                         "match_count": len(matches),
#                         "line_snippet": line.strip()
#                     })

#                 if file_matches:
#                     extracted_snippet = [ matches['line_snippet'] for matches in file_matches ]
#                     link_groups = []
#                     for link_text in extracted_snippet:
#                         match_link = re.search(r'https?://[^\s)"\'<>]+', link_text)
#                         if match_link:
#                             link =  match_link.group()
#                             link_groups.append(link)
#                     for text_link in link_groups:
#                         if text_link in result:
#                             result[text_link] += 1
#                         else:
#                             result[text_link] = 1


#         return result

#     except Exception as e:
#         raise FileAccessError(f"Error during directory search: {e}")

    
# def search_texts_markdown(query: str) -> dict:
#     """
#     Searches all .txt files in target_dir for a given word or phrase.
#     Supports case-insensitive exact phrase matching and line-level reporting.
#     """

#     try:
#         link_grouped =  []
#         result = {}

#         for line in query.splitlines():
#             links = re.findall(r'https?://[^\s)"\'<>]+', line)
#             for link in links:
#                 link_grouped.append(link.strip())


#         for text_link in link_grouped:
#             if text_link in result:
#                 result[text_link] += 1
#             else:
#                 result[text_link] = 1

#         return result

#     except Exception as e:
#         raise FileAccessError(f"Error during directory search: {e}")


# def run_text_searcher() -> None:
#     """Main CLI loop for Text File Searcher Engine."""
#     print("=" * 45)
#     print("       MARKDOWN/HTML LINK EXTRACTOR")
#     print("=" * 45)
#     print("Commands:")
#     print("  'file'       -> Extract links from a file")
#     print("  'text'       -> Enter text directly")
#     print("  'exit'/'quit' -> Exit program")
#     print("-" * 45)


#     while True:
#         try:
#             raw_input = input("\nDo you want to extract links from a file or text? (file/text)  > ").strip().lower()

#             if not raw_input :
#                 continue

   
#             if raw_input.lower() in ("exit", "quit"):
#                 print("Exiting Text Searcher. Goodbye!")
#                 break

                    
#             match raw_input:
#                 case "file" | "f":
#                     file_input = input("\nType the name of the file  > ").strip().lower()
#                     search_results = search_file_markdown(file_input)
#                 case "text" | "t":
#                     lines = []

#                     print("\nPaste the file content below.")
#                     print("Type END on a new line when finished:")

#                     while True:
#                         line = input()

#                         if line.lower() == "end":
#                             break

#                         lines.append(line)

#                     texts_input = "\n".join(lines)
#                     search_results = search_texts_markdown(texts_input)
#                 case _:
#                     raise InvalidInputError("Kindly type between file/text")


    

#             # Display Search Results
#             print(f"\n--- Search Results for '{raw_input}' ---")
            
#             if not search_results:
#                 print("No matches found across .txt files.")
#                 continue


#             for link, count_times in search_results.items():
#                 print(f"{link} appears {count_times} times")
                

#         except TextSearcherError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     run_text_searcher()




# ============================================= AFTER AI REVIEW



import re
from pathlib import Path


class MarkdownExtractorError(Exception):
    """Base exception class for Markdown/HTML Link Extractor domain errors."""
    pass


class InvalidInputError(MarkdownExtractorError):
    """Raised when user search query or input is invalid."""
    pass


class FileAccessError(MarkdownExtractorError):
    """Raised when file scanning or reading fails."""
    pass


# Robust regex pattern for HTTP/HTTPS links in Markdown and HTML
LINK_REGEX = r'https?://[^\s)"\'<>]+'


def extract_links_from_text(text: str) -> dict[str, int]:
    """
    Extracts all URLs from a given text string and returns a frequency dictionary.
    """
    if not text.strip():
        raise InvalidInputError("Provided text is empty.")

    link_counts = {}
    matches = re.findall(LINK_REGEX, text)

    for link in matches:
        clean_link = link.strip(".,;:?!")  
        link_counts[clean_link] = link_counts.get(clean_link, 0) + 1

    return link_counts


def extract_links_from_file(file_name: str, target_dir: Path | None = None) -> dict[str, int]:
    """
    Scans supported files (.md, .html, .htm, .txt) for links and returns their frequencies.
    """
    clean_name = file_name.strip()
    if not clean_name:
        raise InvalidInputError("Filename cannot be empty.")

    search_path = target_dir if target_dir else Path(__file__).parent
    if not search_path.exists() or not search_path.is_dir():
        raise FileAccessError(f"Search directory '{search_path}' does not exist.")

    # Find file matching stem name across supported extensions
    allowed_extensions = (".md", ".html", ".htm", ".txt")
    target_file = None

    for ext in allowed_extensions:
        potential_path = search_path / f"{Path(clean_name).stem}{ext}"
        if potential_path.is_file():
            target_file = potential_path
            break

    if not target_file:
        raise FileAccessError(f"No supported file matching '{clean_name}' found in directory.")

    try:
        with open(target_file, "r", encoding="utf-8", errors="ignore") as file_handle:
            content = file_handle.read()
            return extract_links_from_text(content)
    except Exception as e:
        raise FileAccessError(f"Failed to read file '{target_file.name}': {e}")


def run_link_extractor() -> None:
    """Main CLI loop for the Markdown/HTML Link Extractor."""
    print("=" * 45)
    print("       MARKDOWN/HTML LINK EXTRACTOR CLI")
    print("=" * 45)
    print("Commands:")
    print("  'file' / 'f'  -> Extract links from a file")
    print("  'text' / 't'  -> Paste text directly")
    print("  'exit'/'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("\nExtract links from file or text? (file/text) > ").strip().lower()

            if not raw_input:
                continue

            if raw_input in ("exit", "quit"):
                print("Exiting Link Extractor. Goodbye!")
                break

            match raw_input:
                case "file" | "f":
                    file_input = input("Type the name of the file (e.g., readme.md) > ").strip()
                    link_results = extract_links_from_file(file_input)
                case "text" | "t":
                    print("\nPaste your content below. Type END on a new line when finished:")
                    lines = []
                    while True:
                        line = input()
                        if line.strip().lower() == "end":
                            break
                        lines.append(line)
                    text_content = "\n".join(lines)
                    link_results = extract_links_from_text(text_content)
                case _:
                    raise InvalidInputError("Please type either 'file' or 'text'.")

            print(f"\n--- Extraction Results ---")
            if not link_results:
                print("No valid links found.")
                continue

            total_links = sum(link_results.values())
            print(f"Found {total_links} total reference(s) ({len(link_results)} unique link(s)):\n")

            for link, count in link_results.items():
                print(f"  • {link}  ({count} time(s))")

        except MarkdownExtractorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_link_extractor()