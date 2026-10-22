from pathlib import Path
import hashlib


class DuplicateFinderError(Exception):
    """Base exception for Duplicate Finder domain errors."""
    pass


class InvalidInputError(DuplicateFinderError):
    """Raised when user input is invalid."""
    pass


class DirectoryNotFoundError(DuplicateFinderError):
    """Raised when a target folder does not exist."""
    pass


class StorageError(DuplicateFinderError):
    """Raised when reading files or hashing fails."""
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


def calculate_file_hash(file_path: Path, chunk_size: int = 65536) -> str:
    """Compute the SHA-256 hash of a file in binary chunks for performance."""
    
    hasher = hashlib.sha256()
    try:
        with file_path.open("rb") as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                hasher.update(chunk)
        return hasher.hexdigest()
    except OSError as err:
        raise StorageError(f"Failed to read file '{file_path.name}' for hashing: {err}") from err


def find_duplicate_files(loaded_folder_path: Path) -> dict[str, list[Path]]:
    """Scan directory, compute binary hashes, and group duplicate files."""
    hash_map: dict[str, list[Path]] = {}

    try:
        files = sorted(f for f in loaded_folder_path.iterdir() if f.is_file())

        if not files:
            return hash_map

        for file in files:
            file_hash = calculate_file_hash(file)
            if file_hash not in hash_map:
                hash_map[file_hash] = []
            hash_map[file_hash].append(file)

        duplicates = {h: paths for h, paths in hash_map.items() if len(paths) > 1}
        return duplicates

    except OSError as err:
        raise StorageError(f"Failed to scan directory for duplicates: {err}") from err


def file_duplicate_finder_generator() -> None:
    """Run the main Duplicate File Finder CLI loop."""
    print("=" * 45)
    print("             DUPLICATE FILE FINDER")
    print("=" * 45)

    loaded_directory = None

    while True:
        folder_name = input("\nEnter the folder name to scan for duplicates: ").strip()
        if not folder_name:
            print("Folder name cannot be empty. Please try again.")
            continue

        try:
            loaded_directory = load_file_directory(folder_name)
            file_count = sum(1 for f in loaded_directory.iterdir() if f.is_file())
            print(f"Successfully loaded folder '{loaded_directory.name}' with {file_count} file(s).")
            break
        except DuplicateFinderError as err:
            print(f"Error: {err}")
            print("Please check the folder name and try again.\n")

    print("\nInstructions:")
    print("  -> Scans all files using binary SHA-256 content hashing.")
    print("  -> Identifies exact file duplicates regardless of filenames.")
    print("  -> Type 'yes' to scan or 'exit' to quit.")
    print("-" * 45)

    while True:
        try:
            reply = input("\nProceed to scan for duplicates? (yes/no) > ").strip().lower()

            if not reply:
                continue

            if reply in ("exit", "quit"):
                print("Exiting Duplicate File Finder. Goodbye!")
                break

            if reply not in ("no", "yes"):
                print("Please answer with 'yes' or 'no'.")
                continue

            if reply == "no":
                print("Scan cancelled.")
                continue


            if reply == "yes":
                duplicates = find_duplicate_files(loaded_directory)

                if duplicates:
                    total_duplicate_sets = len(duplicates)
                    print(f"\nFound {total_duplicate_sets} set(s) of duplicate files:")

                    for file_hash, paths in duplicates.items():
                        print(f"\n  🔐 Hash Group ({file_hash[:10]}...):")
                        
                        ext_groups = {}
                        for path in paths:
                            ext = path.suffix.lstrip(".").lower() or "no_extension"
                            if ext not in ext_groups:
                                ext_groups[ext] = []
                            ext_groups[ext].append(path)

                        for ext, ext_paths in ext_groups.items():
                            print(f"     Extension Group of: .{ext}")
                            for path in ext_paths:
                                print(f"        • {path.name}")
                else:
                    print("\nNo duplicate files found! All files are unique.")
        except DuplicateFinderError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    file_duplicate_finder_generator()