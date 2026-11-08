

# import csv
# from pathlib import Path


# class BulkFileRenameError(Exception):
#     """Base exception for CSV Data Cleaner domain errors."""
#     pass


# class InvalidInputError(BulkFileRenameError):
#     """Raised when user input is invalid."""
#     pass


# class CsvFileNotFoundError(BulkFileRenameError):
#     """Raised when a CSV file does not exist or is empty."""
#     pass


# class StorageError(BulkFileRenameError):
#     """Raised when loading or saving CSV data fails."""
#     pass


# DATA_DIR = Path(__file__).parent



# def parse_and_format_date(date_str: str) -> str:
#     """Try parsing date string across common formats and standardize to YYYY-MM-DD.
#     Returns empty string if invalid or 'not available'."""


#     date_str = date_str.strip()
#     if not date_str or date_str.lower() in ("not available", "n/a", "none", "null"):
#         return ""
    
#     formats = [
#         "%Y-%m-%d", 
#         "%m/%d/%Y",  
#         "%d/%m/%Y",  
#         "%Y/%m/%d", 
#         "%d-%m-%Y",  
#     ]
    
#     for fmt in formats:
#         try:
#             parsed_date = datetime.strptime(date_str, fmt)
#             return parsed_date.strftime("%Y-%m-%d")
#         except ValueError:
#             continue
            
#     return ""


# def load_file_directory(foldername: str) -> list[dict]:
#     """Load data from a CSV file into a list of dictionaries using DictReader."""
#     clean_name = foldername.strip()

#     data_file = DATA_DIR / clean_name

#     if data_file.is_dir() and data_file.name == clean_name:
#         return data_file
#     else:
#         raise BulkFileRenameError("Folder doesn't existes")

    
    
    


#     # if not data_file.suffix:
#     #     data_file = data_file.with_suffix(".log")

#     # if not data_file.is_file():
#     #     raise CsvFileNotFoundError(f"log file not found: {data_file.name}")    

#     # try:
#     #     with open(data_file, "r", encoding="utf-8", newline="") as f:
#     #         reader = f.readlines()
#     #         data = list(reader)
#     #         if not data:
#     #             raise CsvFileNotFoundError(f"The log file '{data_file.name}' is empty.")
#     #         return data
#     # except Exception as err:
#     #     raise StorageError(f"Failed to load log file '{data_file.name}': {err}") from err


    

# def process_file_cleaner_action(
#     name_sequence_style: str,
#     loaded_folder_path: Path,
# ) -> list[Path]:
#     """Rename files using the specified naming prefix."""

#     if not name_sequence_style.strip():
#         raise BulkFileRenameError("Name format can't be empty")

#     renamed_files = []

#     for index, file in enumerate(loaded_folder_path.iterdir(), start=1):
#         if file.is_file():
#             new_name = f"{name_sequence_style.strip()}{index}{file.suffix}"
#             new_file = file.with_name(new_name)
#             file.rename(new_file)
#             renamed_files.append(new_file)

#     return renamed_files

# def bulk_file_renamer() -> None:
#     """Run the main CSV Data Cleaner CLI loop."""
#     print("=" * 45)
#     print("                 CSV DATA CLEANER")
#     print("=" * 45)

#     folder_name = ""

#     while True:
#         folder_name = input("\nEnter the folder name you wants to renamer from: ").strip()
#         if not folder_name:
#             print("File name cannot be empty. Please try again.")
#             continue

#         try:
#             # print(folder_name)
#             loaded_directory = load_file_directory(folder_name)
#             print(loaded_directory)
#             print(f"Successfully Founded '{folder_name}' with 5 files.")
#             break
#         except BulkFileRenameError as err:
#             print(f"Error: {err}")
#             print("Please check the filename and try again.\n")

#     print("\nActions:")
#     print("  load     -> Load a CSV file")
#     print("  view     -> View CSV data preview")
#     print("  clean    -> Clean whitespace from data")
#     print("  validate -> Validate numerical fields")
#     print("  missing  -> Check for missing columns and values")
#     print("  save     -> Save cleaned data to a new file")
#     print("  exit     -> Exit program")
#     print("-" * 45)

#     while True:
#         try:
#             name_sequence_style = input("\nWhat do you wants to rename the files to (specify with index1 , prod1) sequence approach? > ").strip().lower()

#             if not name_sequence_style:
#                 continue

#             if name_sequence_style in ("exit", "quit"):
#                 print("Exiting CSV Data Cleaner. Goodbye!")
#                 break

#             loaded_file = process_file_cleaner_action(name_sequence_style, loaded_directory)

#             print(loaded_file)

#         except BulkFileRenameError as err:
#             print(f"Error: {err}")
#         except ( KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     bulk_file_renamer()
















from pathlib import Path


class BulkFileRenameError(Exception):
    """Base exception for Bulk File Renamer domain errors."""
    pass


class InvalidInputError(BulkFileRenameError):
    """Raised when user input is invalid."""
    pass


class DirectoryNotFoundError(BulkFileRenameError):
    """Raised when a target folder does not exist."""
    pass


class StorageError(BulkFileRenameError):
    """Raised when file renaming operations fail."""
    pass


DATA_DIR = Path(__file__).parent


def load_file_directory(foldername: str) -> Path:
    """Validate and return the target folder path."""
    clean_name = foldername.strip()
    if not clean_name:
        raise InvalidInputError("Folder name cannot be empty.")

    folder_path = DATA_DIR / clean_name

    if folder_path.is_dir():
        return folder_path
    else:
        raise DirectoryNotFoundError(f"The folder '{clean_name}' does not exist.")


def process_batch_renaming(
    name_sequence_style: str,
    loaded_folder_path: Path,
) -> list[Path]:
    """Rename files in the target directory using the specified naming prefix."""
    prefix = name_sequence_style.strip()
    if not prefix:
        raise InvalidInputError("Naming format/prefix cannot be empty.")

    renamed_files = []

    try:
        files = [f for f in loaded_folder_path.iterdir() if f.is_file()]
        
        if not files:
            print("No files found inside this directory to rename.")
            return renamed_files

        for index, file in enumerate(files, start=1):
            new_name = f"{prefix}_{index}{file.suffix}"
            new_file = file.with_name(new_name)
            file.rename(new_file)
            renamed_files.append(new_file)

        return renamed_files
    except OSError as err:
        raise StorageError(f"Failed to rename files: {err}") from err


def bulk_file_renamer() -> None:
    """Run the main Bulk File Renamer CLI loop."""
    print("=" * 45)
    print("             BULK FILE RENAMER")
    print("=" * 45)

    loaded_directory = None

    while True:
        folder_name = input("\nEnter the folder name to target: ").strip()
        if not folder_name:
            print("Folder name cannot be empty. Please try again.")
            continue

        try:
            loaded_directory = load_file_directory(folder_name)
            file_count = sum(1 for f in loaded_directory.iterdir() if f.is_file())
            print(f"Successfully loaded folder '{loaded_directory.name}' with {file_count} file(s).")
            break
        except BulkFileRenameError as err:
            print(f"Error: {err}")
            print("Please check the folder name and try again.\n")

    print("\nInstructions:")
    print("  -> Enter a prefix (e.g., 'invoice', 'photo', 'project')")
    print("  -> Files will automatically be renamed as prefix_1.ext, prefix_2.ext, etc.")
    print("  -> Type 'exit' or 'quit' to close the program.")
    print("-" * 45)

    while True:
        try:
            name_sequence_style = input("\nEnter naming prefix > ").strip()

            if not name_sequence_style:
                continue

            if name_sequence_style.lower() in ("exit", "quit"):
                print("Exiting Bulk File Renamer. Goodbye!")
                break

            renamed = process_batch_renaming(name_sequence_style, loaded_directory)
            
            if renamed:
                print(f"\nSuccessfully renamed {len(renamed)} file(s):")
                for path in renamed:
                    print(f"  • {path.name}")

        except BulkFileRenameError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    bulk_file_renamer()
