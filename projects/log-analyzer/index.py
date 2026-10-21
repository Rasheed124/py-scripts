

# import csv
# from pathlib import Path


# class CsvCleanerError(Exception):
#     """Base exception for CSV Data Cleaner domain errors."""
#     pass


# class InvalidInputError(CsvCleanerError):
#     """Raised when user input is invalid."""
#     pass


# class CsvFileNotFoundError(CsvCleanerError):
#     """Raised when a CSV file does not exist or is empty."""
#     pass


# class StorageError(CsvCleanerError):
#     """Raised when loading or saving CSV data fails."""
#     pass


# DATA_DIR = Path(__file__).parent


# from datetime import datetime


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


# def load_csv_file(filename: str) -> list[dict]:
#     """Load data from a CSV file into a list of dictionaries using DictReader."""
#     clean_name = filename.strip()
#     data_file = DATA_DIR / clean_name

#     if not data_file.suffix:
#         data_file = data_file.with_suffix(".log")

#     if not data_file.is_file():
#         raise CsvFileNotFoundError(f"log file not found: {data_file.name}")    

#     try:
#         with open(data_file, "r", encoding="utf-8", newline="") as f:
#             reader = f.readlines()
#             data = list(reader)
#             if not data:
#                 raise CsvFileNotFoundError(f"The log file '{data_file.name}' is empty.")
#             return data
#     except Exception as err:
#         raise StorageError(f"Failed to load log file '{data_file.name}': {err}") from err


#     return data_file
    


# def process_file_cleaner_action(file_name: str, loaded_file: list[dict], action: str) -> list[dict]:
#     """Perform actions on the loaded CSV dataset."""

#     if action == "load":
#         loaded_file = load_csv_file(file_name)
#         print(f"\nSuccessfully reloaded {len(loaded_file)} row(s) from '{file_name}'.")

#     elif action == "view":
#         if not loaded_file:
#             print("\nNo data currently loaded.")
#             return loaded_file

#         for row_number, row in enumerate(loaded_file, start=1):
#             print(f"Row {row_number}: {row.strip()}")

#     elif action == "log":
#         print("\n--- Cleaning Dataset (Standardizing Gender & Dates) ---")
#         cleaned_rows_count = 0
#         fields_modified_count = 0

#         logs_files_issues = {}

#         for row_number, row in enumerate(loaded_file, start=1):
#             row = row.strip()

#             if "INFO" in row:
#                 log_level = "INFO"
#             elif "WARNING" in row:
#                 log_level = "WARNING"
#             elif "ERROR" in row:
#                 log_level = "ERROR"
#             else:
#                 continue

#             if log_level in logs_files_issues:
#                 logs_files_issues[log_level] += 1
#             else:
#                 logs_files_issues[log_level] = 1

#         print(logs_files_issues)
#         print(f"Cleaning complete! Standardized/cleared {fields_modified_count} field(s) across {cleaned_rows_count} row(s).")


#     return loaded_file


# def log_file_analyzer_generator() -> None:
#     """Run the main CSV Data Cleaner CLI loop."""
#     print("=" * 45)
#     print("                 CSV DATA CLEANER")
#     print("=" * 45)

#     loaded_file = []
#     file_name = ""

#     while True:
#         file_name = input("\nEnter the log file name to load: ").strip()
#         if not file_name:
#             print("File name cannot be empty. Please try again.")
#             continue

#         try:
#             # print(file_name)
#             loaded_file = load_csv_file(file_name)
     
#             print(f"Successfully loaded '{file_name}' with {len(loaded_file)} records.")
#             break
#         except CsvCleanerError as err:
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
#             action = input("\nWhat action would you like to perform? > ").strip().lower()

#             if not action:
#                 continue

#             if action in ("exit", "quit"):
#                 print("Exiting CSV Data Cleaner. Goodbye!")
#                 break

#             valid_actions = ("load", "view", "log", "validate", "missing", "save")

#             if action not in valid_actions:
#                 raise InvalidInputError(
#                     "Invalid action. Choose load, view, clean, validate, missing, save, or exit."
#                 )

#             loaded_file = process_file_cleaner_action(file_name, loaded_file, action)

#         except CsvCleanerError as err:
#             print(f"Error: {err}")
#         except ( KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     log_file_analyzer_generator()








from pathlib import Path
from datetime import datetime
from collections import Counter
import re


class LogAnalyzerError(Exception):
    """Base exception for log analyzer errors."""


class InvalidInputError(LogAnalyzerError):
    """Raised when user input is invalid."""


class LogFileNotFoundError(LogAnalyzerError):
    """Raised when a log file does not exist or is empty."""


class StorageError(LogAnalyzerError):
    """Raised when reading or writing a log file fails."""


DATA_DIR = Path(__file__).parent

LOG_LEVELS = ("INFO", "WARNING", "ERROR", "DEBUG", "CRITICAL")
MISSING_VALUES = ("not available", "n/a", "none", "null")


def parse_and_format_date(date_str: str) -> str:
    """Parse common date formats and return YYYY-MM-DD.

    Return an empty string if the date is missing or invalid.
    """
    if not date_str or date_str.strip().lower() in MISSING_VALUES:
        return ""

    date_str = date_str.strip()

    formats = (
        "%Y-%m-%d",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%Y/%m/%d",
        "%d-%m-%Y",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
    )

    for date_format in formats:
        try:
            parsed_date = datetime.strptime(date_str, date_format)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            continue

    return ""


def resolve_file_path(filename: str) -> Path:
    """Resolve a filename inside the application's data directory."""
    clean_name = filename.strip()

    if not clean_name:
        raise InvalidInputError("File name cannot be empty.")

    if Path(clean_name).name != clean_name:
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


def get_log_level(line: str) -> str | None:
    """Extract a recognized log level from a log entry."""
    match = re.search(
        r"\b(INFO|WARNING|ERROR|DEBUG|CRITICAL)\b",
        line,
        re.IGNORECASE,
    )

    return match.group(1).upper() if match else None


def analyze_logs(log_entries: list[str]) -> Counter:
    """Count occurrences of each recognized log level."""
    counts = Counter()

    for entry in log_entries:
        level = get_log_level(entry)

        if level:
            counts[level] += 1

    return counts


def view_logs(log_entries: list[str]) -> None:
    """Display all loaded log entries."""
    if not log_entries:
        print("\nNo log entries are currently loaded.")
        return

    print("\n--- Log File Preview ---")

    for number, entry in enumerate(log_entries, start=1):
        print(f"{number:>4}: {entry}")

    print(f"\nTotal entries: {len(log_entries)}")


def clean_logs(log_entries: list[str]) -> list[str]:
    """Remove leading and trailing whitespace from log entries."""
    cleaned_entries = []
    modified_count = 0

    for entry in log_entries:
        cleaned_entry = entry.strip()

        if cleaned_entry != entry:
            modified_count += 1

        cleaned_entries.append(cleaned_entry)

    print("\n--- Log Cleaning Results ---")
    print(f"Entries processed: {len(log_entries)}")
    print(f"Entries modified: {modified_count}")

    return cleaned_entries


def display_log_analysis(log_entries: list[str]) -> None:
    """Display log-level counts and a summary of errors."""
    counts = analyze_logs(log_entries)

    print("\n--- Log Analysis Report ---")
    print(f"Total entries: {len(log_entries)}")
    print("-" * 35)

    for level in LOG_LEVELS:
        print(f"{level:<10}: {counts.get(level, 0)}")

    unclassified = sum(
        1 for entry in log_entries if get_log_level(entry) is None
    )
    print(f"{'UNKNOWN':<10}: {unclassified}")

    print("-" * 35)
    print(f"Errors and critical events: "
          f"{counts.get('ERROR', 0) + counts.get('CRITICAL', 0)}")


def validate_logs(log_entries: list[str]) -> None:
    """Validate log entries for dates and recognized log levels."""
    invalid_levels = []
    invalid_dates = []

    date_pattern = re.compile(
        r"\b\d{4}-\d{2}-\d{2}\b"
        r"|\b\d{1,2}/\d{1,2}/\d{4}\b"
        r"|\b\d{1,2}-\d{1,2}-\d{4}\b"
    )

    for number, entry in enumerate(log_entries, start=1):
        if not get_log_level(entry):
            invalid_levels.append(number)

        date_match = date_pattern.search(entry)

        if date_match and not parse_and_format_date(date_match.group()):
            invalid_dates.append(number)

    print("\n--- Log Validation Report ---")
    print(f"Entries checked: {len(log_entries)}")
    print(f"Entries with unrecognized levels: {len(invalid_levels)}")
    print(f"Entries with invalid dates: {len(invalid_dates)}")

    if invalid_levels:
        print(f"Missing/unrecognized levels on lines: {invalid_levels}")

    if invalid_dates:
        print(f"Invalid dates on lines: {invalid_dates}")

    if not invalid_levels and not invalid_dates:
        print("All entries passed the available validation checks.")


def check_missing_data(log_entries: list[str]) -> None:
    """Identify empty entries and entries without log levels."""
    empty_lines = []
    missing_levels = []

    for number, entry in enumerate(log_entries, start=1):
        if not entry.strip():
            empty_lines.append(number)
        elif not get_log_level(entry):
            missing_levels.append(number)

    print("\n--- Missing Data Report ---")
    print(f"Empty lines: {len(empty_lines)}")
    print(f"Entries missing a recognized log level: {len(missing_levels)}")

    if empty_lines:
        print(f"Empty line numbers: {empty_lines}")

    if missing_levels:
        print(f"Unclassified line numbers: {missing_levels}")


def save_logs(log_entries: list[str], filename: str) -> None:
    """Save log entries to a new file in the data directory."""
    file_path = resolve_file_path(filename)

    if file_path.exists() and file_path.resolve() == resolve_file_path(
        filename
    ).resolve():
        # The requested output path is checked separately below.
        pass

    try:
        with file_path.open("w", encoding="utf-8", newline="\n") as file:
            for entry in log_entries:
                file.write(entry + "\n")

        print(
            f"\nSuccessfully saved {len(log_entries)} entries "
            f"to '{file_path.name}'."
        )

    except (OSError, UnicodeError) as err:
        raise StorageError(
            f"Could not save '{file_path.name}': {err}"
        ) from err


def process_log_action(
    filename: str,
    log_entries: list[str],
    action: str,
) -> list[str]:
    """Execute the selected log analyzer action."""

    
    if action == "load":
        log_entries = load_log_file(filename)
        print(
            f"\nSuccessfully loaded {len(log_entries)} entries "
            f"from '{filename}'."
        )

    elif action == "view":
        view_logs(log_entries)

    elif action == "log":
        display_log_analysis(log_entries)

    elif action == "clean":
        log_entries = clean_logs(log_entries)

    elif action == "validate":
        validate_logs(log_entries)

    elif action == "missing":
        check_missing_data(log_entries)

    elif action == "save":
        output_name = input(
            "Enter output filename (e.g. cleaned.log): "
        ).strip()

        if not output_name:
            raise InvalidInputError("Output filename cannot be empty.")

        save_logs(log_entries, output_name)

    return log_entries


def log_file_analyzer_generator() -> None:
    """Run the Log File Analyzer command-line interface."""
    print("=" * 45)
    print("             LOG FILE ANALYZER")
    print("=" * 45)

    filename = ""

    while True:
        filename = input(
            "\nEnter the log file name to load: "
        ).strip()

        try:
            log_entries = load_log_file(filename)
            print(
                f"Successfully loaded '{filename}' "
                f"with {len(log_entries)} entries."
            )
            break

        except LogAnalyzerError as err:
            print(f"Error: {err}")
            print("Please check the filename and try again.")

    print("\nAvailable Actions")
    print("-" * 45)
    print("  load     -> Reload the current log file")
    print("  view     -> View all log entries")
    print("  log      -> Analyze log levels")
    print("  clean    -> Remove surrounding whitespace")
    print("  validate -> Validate log levels and dates")
    print("  missing  -> Find empty or unclassified entries")
    print("  save     -> Save entries to a new file")
    print("  exit     -> Exit the program")
    print("-" * 45)

    valid_actions = {
        "load", "view", "log", "clean",
        "validate", "missing", "save",
    }

    while True:
        try:
            action = input(
                "\nWhat action would you like to perform? > "
            ).strip().lower()

            if not action:
                continue

            if action in ("exit", "quit"):
                print("Exiting Log File Analyzer. Goodbye!")
                break

            if action not in valid_actions:
                raise InvalidInputError(
                    "Invalid action. Choose load, view, log, clean, "
                    "validate, missing, save, or exit."
                )

            log_entries = process_log_action(
                filename, log_entries, action
            )

        except LogAnalyzerError as err:
            print(f"Error: {err}")

        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    log_file_analyzer_generator()