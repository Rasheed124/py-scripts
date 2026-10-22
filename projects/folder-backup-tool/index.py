from pathlib import Path
import shutil
from datetime import datetime


class BackupToolError(Exception):
    """Base exception for Folder Backup Tool domain errors."""
    pass


class InvalidInputError(BackupToolError):
    """Raised when user input is invalid."""
    pass


class DirectoryNotFoundError(BackupToolError):
    """Raised when a target folder does not exist."""
    pass


class StorageError(BackupToolError):
    """Raised when file copying or directory creation fails."""
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


def process_batch_backup(loaded_folder_path: Path) -> dict[str, list[Path]]:
    """Backup files into a timestamped directory using shutil.copy2 to preserve metadata."""
    backed_up_files: dict[str, list[Path]] = {"backup": []}

    try:
        files = sorted(f for f in loaded_folder_path.iterdir() if f.is_file())

        if not files:
            return backed_up_files

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backup_folder_name = f"{loaded_folder_path.name}_backup_{timestamp}"
        backup_folder = loaded_folder_path.parent / backup_folder_name
        backup_folder.mkdir(exist_ok=True)

        for file in files:
            destination = backup_folder / file.name
            
            shutil.copy2(file, destination)
            backed_up_files["backup"].append(destination)

        return backed_up_files

    except OSError as err:
        raise StorageError(f"Failed to backup files: {err}") from err


def folder_backup_tool() -> None:
    """Run the main Folder Backup Tool CLI loop."""
    print("=" * 45)
    print("              FOLDER BACKUP TOOL")
    print("=" * 45)

    loaded_directory = None

    while True:
        folder_name = input("\nEnter the folder name to backup: ").strip()
        if not folder_name:
            print("Folder name cannot be empty. Please try again.")
            continue

        try:
            loaded_directory = load_file_directory(folder_name)
            file_count = sum(1 for f in loaded_directory.iterdir() if f.is_file())
            print(f"Successfully loaded folder '{loaded_directory.name}' with {file_count} file(s).")
            break
        except BackupToolError as err:
            print(f"Error: {err}")
            print("Please check the folder name and try again.\n")

    print("\nInstructions:")
    print("  -> Creates a timestamped backup copy of all files.")
    print("  -> Type 'yes' to proceed with backup or 'no' to cancel.")
    print("  -> Type 'exit' or 'quit' to close the program.")
    print("-" * 45)

    while True:
        try:
            reply = input("\nProceed to backup files? (yes/no) > ").strip().lower()

            if not reply:
                continue

            if reply in ("exit", "quit"):
                print("Exiting Folder Backup Tool. Goodbye!")
                break

            if reply not in ("no", "yes"):
                print("Please answer with 'yes' or 'no'.")
                continue

            if reply == "no":
                print("Backup cancelled.")
                continue

            if reply == "yes":
                backup_results = process_batch_backup(loaded_directory)
                paths = backup_results.get("backup", [])

                if paths:
                    print(f"\nSuccessfully backed up {len(paths)} file(s):")
                    print(f"  📁 Destination: {paths[0].parent.name}/")
                    for path in paths:
                        print(f"     • {path.name}")
                else:
                    print("No files found to backup in this directory.")

        except BackupToolError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    folder_backup_tool()