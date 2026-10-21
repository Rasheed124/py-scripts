
from exceptions import (
    InvalidInputError,
    LogAnalyzerError,
)
from services.file_service import load_log_file, save_logs
from services.cleaning_service import clean_logs
from services.validation_service import (
    validate_logs,
    check_missing_data,
)
from reports.report_service import (
    view_logs,
    display_log_analysis,
    display_cleaning_report,
    display_validation_report,
    display_missing_data_report,
)
from cli.menu import display_menu, display_welcome


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
        original_entries = log_entries.copy()
        log_entries = clean_logs(log_entries)
        display_cleaning_report(original_entries, log_entries)

    elif action == "validate":
        results = validate_logs(log_entries)
        display_validation_report(results)

    elif action == "missing":
        results = check_missing_data(log_entries)
        display_missing_data_report(results)

    elif action == "save":
        output_name = input(
            "Enter output filename (e.g. cleaned.log): "
        ).strip()

        if not output_name:
            raise InvalidInputError(
                "Output filename cannot be empty."
            )

        save_logs(log_entries, output_name)
        print(
            f"\nSuccessfully saved {len(log_entries)} entries "
            f"to '{output_name}'."
        )

    return log_entries


def log_file_analyzer_generator() -> None:
    """Run the Log File Analyzer command-line interface."""
    display_welcome()

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

        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            return

    display_menu()

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

            if action not in {
                "load", "view", "log", "clean",
                "validate", "missing", "save",
            }:
                raise InvalidInputError(
                    "Invalid action. Choose load, view, log, "
                    "clean, validate, missing, save, or exit."
                )

            log_entries = process_log_action(
                filename, log_entries, action
            )

        except LogAnalyzerError as err:
            print(f"Error: {err}")

        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break
