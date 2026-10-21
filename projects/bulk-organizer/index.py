# from pathlib import Path


# class BulkExtensionError(Exception):
#     """Base exception for Bulk Extension Changer domain errors."""
#     pass


# class InvalidInputError(BulkExtensionError):
#     """Raised when user input is invalid."""
#     pass


# class DirectoryNotFoundError(BulkExtensionError):
#     """Raised when a target folder does not exist."""
#     pass


# class StorageError(BulkExtensionError):
#     """Raised when file renaming operations fail."""
#     pass


# DATA_DIR = Path(__file__).parent


# def load_file_directory(foldername: str) -> Path:
#     """Validate and return the target folder path."""
#     clean_name = foldername.strip()
#     if not clean_name:
#         raise InvalidInputError("Folder name cannot be empty.")

#     folder_path = DATA_DIR / clean_name

#     if folder_path.is_dir():
#         return folder_path
#     else:
#         raise DirectoryNotFoundError(f"The folder '{clean_name}' does not exist.")


# def process_batch_organizing(
#     reply: str,
#     loaded_folder_path: Path,
# ) -> dict[str, set[Path]]:
#     """Group files by their extensions."""

#     reply_ans = reply.strip()

#     if not reply_ans:
#         raise InvalidInputError("File extension cannot be empty.")

#     organized_files: dict[str, set[Path]] = {}

#     try:
#         files = sorted(
#             f for f in loaded_folder_path.iterdir()
#             if f.is_file()
#         )

#         for file in files:
#             extension = file.suffix.lstrip(".")

#             if extension not in organized_files:
#                 organized_files[extension] = set()

#             organized_files[extension].add(file)

#         return organized_files

#     except OSError as err:
#         raise StorageError(
#             f"Failed to organize files: {err}"
#         ) from err

# def file_organizer_generator() -> None:
#     """Run the main Bulk File Extension Renamer CLI loop."""
#     print("=" * 45)
#     print("          FILE ORGANIZER GENERATOR")
#     print("=" * 45)

#     loaded_directory = None

#     while True:
#         folder_name = input("\nEnter the folder name to target: ").strip()
#         if not folder_name:
#             print("Folder name cannot be empty. Please try again.")
#             continue

#         try:
#             loaded_directory = load_file_directory(folder_name)
#             file_count = sum(1 for f in loaded_directory.iterdir() if f.is_file())
#             print(f"Successfully loaded folder '{loaded_directory.name}' with {file_count} file(s).")
#             break
#         except BulkExtensionError as err:
#             print(f"Error: {err}")
#             print("Please check the folder name and try again.\n")

#     print("\nInstructions:")
#     print("  -> Enter a target extension (e.g., '.txt', 'md', '.png')")
#     print("  -> All files in the directory will have their extensions updated.")
#     print("  -> Type 'exit' or 'quit' to close the program.")
#     print("-" * 45)

#     while True:
#         try:
#             reply = input("\nCan I proceed to organize? Yes or no > ").strip()

#             if not reply:
#                 continue

#             if reply.lower() in ("exit", "quit"):
#                 print("Exiting Bulk File Organizer. Goodbye!")
#                 break

#             if reply.lower() not in ("no", "yes"):
#                 print("Choose between yes or no.")
#                 continue

#             if reply.lower() == "no":
#                 print("Organization cancelled.")
#                 continue

#             if reply.lower() == "yes":
#                 organized_files = process_batch_organizing(reply, loaded_directory)

#                 if organized_files:
#                     total_files = sum(len(file_paths) for file_paths in organized_files.values())

#                     print(f"\nSuccessfully organized {total_files} file(s):")

#                     for ext, file_paths in organized_files.items():
#                         print(f"\n{ext or 'No extension'}:")
#                         for file in sorted(file_paths):
#                             print(f"  {file.name}")
#                 else:
#                     print("No files found to organize.")

#         except BulkExtensionError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     file_organizer_generator()















from pathlib import Path
import shutil


class FileOrganizerError(Exception):
    """Base exception for File Organizer domain errors."""
    pass


class InvalidInputError(FileOrganizerError):
    """Raised when user input is invalid."""
    pass


class DirectoryNotFoundError(FileOrganizerError):
    """Raised when a target folder does not exist."""
    pass


class StorageError(FileOrganizerError):
    """Raised when file moving or directory creation fails."""
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


def process_batch_organizing(loaded_folder_path: Path) -> dict[str, list[Path]]:
    """Group files by extension, create subfolders, and physically move them."""
    organized_files: dict[str, list[Path]] = {}

    try:
        files = sorted(f for f in loaded_folder_path.iterdir() if f.is_file())

        if not files:
            return organized_files

        for file in files:

            ext = file.suffix.lstrip(".").lower()
            if not ext:
                ext = "no_extension"

            subfolder = loaded_folder_path / ext
            subfolder.mkdir(exist_ok=True)

            destination = subfolder / file.name

            if file.resolve() != destination.resolve():
                shutil.move(str(file), str(destination))

            if ext not in organized_files:
                organized_files[ext] = []
            organized_files[ext].append(destination)

        return organized_files

    except OSError as err:
        raise StorageError(f"Failed to organize files: {err}") from err


def file_organizer_generator() -> None:
    """Run the main File Organizer CLI loop."""
    print("=" * 45)
    print("               FILE ORGANIZER")
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
        except FileOrganizerError as err:
            print(f"Error: {err}")
            print("Please check the folder name and try again.\n")

    print("\nInstructions:")
    print("  -> Automatically sorts files into subfolders based on their extensions.")
    print("  -> Type 'yes' to proceed or 'no' to cancel.")
    print("  -> Type 'exit' or 'quit' to close the program.")
    print("-" * 45)

    while True:
        try:
            reply = input("\nProceed to organize files? (yes/no) > ").strip().lower()

            if not reply:
                continue

            if reply in ("exit", "quit"):
                print("Exiting File Organizer. Goodbye!")
                break

            if reply not in ("no", "yes"):
                print("Please answer with 'yes' or 'no'.")
                continue

            if reply == "no":
                print("Organization cancelled.")
                continue

            if reply == "yes":
                organized_files = process_batch_organizing(loaded_directory)

                if organized_files:
                    total_files = sum(len(paths) for paths in organized_files.values())
                    print(f"\nSuccessfully organized {total_files} file(s) into subfolders:")

                    for ext, paths in organized_files.items():
                        print(f"\n  📁 /{ext} ({len(paths)} file(s)):")
                        for path in paths:
                            print(f"     • {path.name}")
                else:
                    print("No files found to organize in this directory.")

        except FileOrganizerError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    file_organizer_generator()