from pathlib import Path


class BulkExtensionError(Exception):
    """Base exception for Bulk Extension Changer domain errors."""
    pass


class InvalidInputError(BulkExtensionError):
    """Raised when user input is invalid."""
    pass


class DirectoryNotFoundError(BulkExtensionError):
    """Raised when a target folder does not exist."""
    pass


class StorageError(BulkExtensionError):
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
    extension_style: str,
    loaded_folder_path: Path,
) -> list[Path]:
    """Change the extensions of files in the target directory."""
    postfix = extension_style.strip()

    if not postfix:
        raise InvalidInputError("File extension cannot be empty.")

    if not postfix.startswith("."):
        postfix = f".{postfix}"

    renamed_files = []

    try:
        files = sorted(f for f in loaded_folder_path.iterdir() if f.is_file())

        if not files:
            print("No files found inside this directory to rename.")
            return renamed_files

        for file in files:
            new_file = file.with_suffix(postfix)

            if new_file.exists() and new_file != file:
                raise StorageError(f"File collision detected: '{new_file.name}' already exists.")

            file.rename(new_file)
            renamed_files.append(new_file)

        return renamed_files

    except OSError as err:
        raise StorageError(f"Failed to rename file extensions: {err}") from err


def bulk_file_extension_renamer() -> None:
    """Run the main Bulk File Extension Renamer CLI loop."""
    print("=" * 45)
    print("          BULK FILE EXTENSION RENAMER")
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
        except BulkExtensionError as err:
            print(f"Error: {err}")
            print("Please check the folder name and try again.\n")

    print("\nInstructions:")
    print("  -> Enter a target extension (e.g., '.txt', 'md', '.png')")
    print("  -> All files in the directory will have their extensions updated.")
    print("  -> Type 'exit' or 'quit' to close the program.")
    print("-" * 45)

    while True:
        try:
            ext_name = input("\nEnter target extension > ").strip()

            if not ext_name:
                continue

            if ext_name.lower() in ("exit", "quit"):
                print("Exiting Bulk File Extension Renamer. Goodbye!")
                break

            renamed_file_extensions = process_batch_renaming(ext_name, loaded_directory)

            if renamed_file_extensions:
                print(f"\nSuccessfully updated extension for {len(renamed_file_extensions)} file(s):")
                for path in renamed_file_extensions:
                    print(f"  • {path.name}")

        except BulkExtensionError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    bulk_file_extension_renamer()