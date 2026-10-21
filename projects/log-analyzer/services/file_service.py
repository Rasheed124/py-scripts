
from pathlib import Path

from config import DATA_DIR
from exceptions import (
    InvalidInputError,
    LogAnalyzerError,
    LogFileNotFoundError,
    StorageError,
)


def resolve_file_path(filename: str) -> Path:
    """Resolve a filename inside the application's data directory."""
    clean_name = filename.strip()

    if not clean_name:
        raise InvalidInputError("File name cannot be empty.")

    if Path(clean_name).name != clean_name or clean_name in {".", ".."}:
        raise InvalidInputError(
            "Please enter a file name without directory paths."
        )

    file_path = DATA_DIR / clean_name

    if not file_path.suffix:
        file_path = file_path.with_suffix(".log")

    return file_path


def load_log_file(filename: str) -> list[str]:
    """Load log entries from a text file."""
    file_path = resolve_file_path(filename)

    if not file_path.is_file():
        raise LogFileNotFoundError(
            f"Log file '{file_path.name}' was not found."
        )

    try:
        with file_path.open("r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            raise LogFileNotFoundError(
                f"Log file '{file_path.name}' is empty."
            )

        return [line.rstrip("\r\n") for line in lines]

    except LogAnalyzerError:
        raise
    except (OSError, UnicodeError) as err:
        raise StorageError(
            f"Could not read '{file_path.name}': {err}"
        ) from err


def save_logs(log_entries: list[str], filename: str) -> None:
    """Save log entries to a file in the data directory."""
    file_path = resolve_file_path(filename)

    try:
        with file_path.open(
            "w", encoding="utf-8", newline="\n"
        ) as file:
            for entry in log_entries:
                file.write(entry + "\n")

    except (OSError, UnicodeError) as err:
        raise StorageError(
            f"Could not save '{file_path.name}': {err}"
        ) from err
