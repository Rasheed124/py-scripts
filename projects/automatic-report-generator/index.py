

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
#         data_file = data_file.with_suffix(".csv")

#     if not data_file.is_file():
#         raise CsvFileNotFoundError(f"CSV file not found: {data_file.name}")

#     try:
#         with open(data_file, "r", encoding="utf-8", newline="") as f:
#             reader = csv.DictReader(f)
#             data = list(reader)
#             if not data:
#                 raise CsvFileNotFoundError(f"The CSV file '{data_file.name}' is empty.")
#             return data
#     except Exception as err:
#         raise StorageError(f"Failed to load CSV file '{data_file.name}': {err}") from err


# def save_csv_file(filename: str, data: list[dict]) -> None:
#     """Save a list of dictionaries back into a CSV file using DictWriter."""
#     if not data:
#         raise InvalidInputError("No data available to save.")

#     clean_name = filename.strip()
#     data_file = DATA_DIR / clean_name
#     if not data_file.suffix:
#         data_file = data_file.with_suffix(".csv")

#     try:
#         with open(data_file, "w", encoding="utf-8", newline="") as f:
#             fieldnames = data[0].keys()
#             writer = csv.DictWriter(f, fieldnames=fieldnames)
#             writer.writeheader()
#             writer.writerows(data)
#         print(f"Data successfully saved to {data_file.name}!")
#     except Exception as err:
#         raise StorageError(f"Failed to save CSV file: {err}") from err


# def process_file_cleaner_action(file_name: str, loaded_file: list[dict], action: str) -> list[dict]:
#     """Perform actions on the loaded CSV dataset."""

#     if action == "load":
#         loaded_file = load_csv_file(file_name)
#         print(f"\nSuccessfully reloaded {len(loaded_file)} row(s) from '{file_name}'.")

#     elif action == "view":
#         if not loaded_file:
#             print("\nNo data currently loaded.")
#             return loaded_file

#         print(f"\n--- Previewing Dataset ({len(loaded_file)} total rows) ---")
#         headers = list(loaded_file[0].keys())
#         header_str = " | ".join(f"{h:<15}" for h in headers)
#         print(header_str)
#         print("-" * len(header_str))

#         for row in loaded_file[:10]:
#             row_str = " | ".join(f"{str(row.get(h, '')):<15}" for h in headers)
#             print(row_str)
#         if len(loaded_file) > 10:
#             print(f"... and {len(loaded_file) - 10} more rows.")

#     elif action == "report":
#         print("\n--- SALES REPORT ---")

#         total_revenue = 0.0
#         total_quantity = 0

#         for row in loaded_file:
#             product_name = row["Product"]
#             product_quantity = int(row["Quantity"])
#             product_price = float(row["Price"])

#             product_total = product_quantity * product_price

#             total_quantity += product_quantity
#             total_revenue += product_total

#             print(f"{product_name:<25} ${product_total:,.2f}")

#         print("-" * 40)
#         print(f"Total Items Sold: {total_quantity}")
#         print(f"Total Revenue: ${total_revenue:,.2f}")


#     return loaded_file



# def automatic_csv_report_generator() -> None:
#     """Run the main CSV Data Cleaner CLI loop."""
#     print("=" * 45)
#     print("                 CSV DATA CLEANER")
#     print("=" * 45)

#     loaded_file = []
#     file_name = ""

#     while True:
#         file_name = input("\nEnter the CSV file name to load: ").strip()
#         if not file_name:
#             print("File name cannot be empty. Please try again.")
#             continue

#         try:
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

#             valid_actions = ("load", "view", "report")

#             if action not in valid_actions:
#                 raise InvalidInputError(
#                     "Invalid action. Choose load, view, report, or exit."
#                 )

#             loaded_file = process_file_cleaner_action(file_name, loaded_file, action)

#         except CsvCleanerError as err:
#             print(f"Error: {err}")
#         except ( KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     automatic_csv_report_generator()














import csv
from pathlib import Path
from datetime import datetime


class ReportGeneratorError(Exception):
    """Base exception for Automatic Report Generator domain errors."""
    pass


class InvalidInputError(ReportGeneratorError):
    """Raised when user input is invalid."""
    pass


class CsvFileNotFoundError(ReportGeneratorError):
    """Raised when a CSV file does not exist or is empty."""
    pass


class StorageError(ReportGeneratorError):
    """Raised when loading CSV data fails."""
    pass


DATA_DIR = Path(__file__).parent



def load_csv_file(filename: str) -> list[dict]:
    """Load data from a CSV file into a list of dictionaries using DictReader."""
    clean_name = filename.strip()
    data_file = DATA_DIR / clean_name
    if not data_file.suffix:
        data_file = data_file.with_suffix(".csv")

    if not data_file.is_file():
        raise CsvFileNotFoundError(f"CSV file not found: {data_file.name}")

    try:
        with open(data_file, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            data = list(reader)
            if not data:
                raise CsvFileNotFoundError(f"The CSV file '{data_file.name}' is empty.")
            return data
    except (OSError, csv.Error) as err:
        raise StorageError(f"Failed to load CSV file '{data_file.name}': {err}") from err


def process_report_action(file_name: str, loaded_file: list[dict], action: str) -> list[dict]:
    """Perform actions on the loaded CSV dataset."""

    if action == "load":
        loaded_file = load_csv_file(file_name)
        print(f"\nSuccessfully reloaded {len(loaded_file)} row(s) from '{file_name}'.")

    elif action == "view":
        if not loaded_file:
            print("\nNo data currently loaded.")
            return loaded_file

        print(f"\n--- Previewing Dataset ({len(loaded_file)} total rows) ---")
        headers = list(loaded_file[0].keys())
        header_str = " | ".join(f"{h:<15}" for h in headers)
        print(header_str)
        print("-" * len(header_str))

        for row in loaded_file[:10]:
            row_str = " | ".join(f"{str(row.get(h, '')):<15}" for h in headers)
            print(row_str)
        if len(loaded_file) > 10:
            print(f"... and {len(loaded_file) - 10} more rows.")

    elif action == "report":
        if not loaded_file:
            print("\nNo data loaded to generate report.")
            return loaded_file

        print("\n" + "=" * 45)
        print("                 SALES REPORT")
        print("=" * 45)

        total_revenue = 0.0
        total_quantity = 0

        print(f"{'Product':<25} | {'Line Total':>15}")
        print("-" * 45)

        for row in loaded_file:
            try:
                product_name = row.get("Product", "Unknown")
                product_quantity = int(row.get("Quantity", 0))
                product_price = float(row.get("Price", 0.0))

                product_total = product_quantity * product_price

                total_quantity += product_quantity
                total_revenue += product_total

                print(f"{product_name:<25} | ${product_total:>14,.2f}")
            except (ValueError, TypeError):
                continue

        print("-" * 45)
        print(f"Total Items Sold: {total_quantity}")
        print(f"Total Revenue:    ${total_revenue:,.2f}")
        print("=" * 45)

    return loaded_file


def automatic_csv_report_generator() -> None:
    """Run the main Automatic Report Generator CLI loop."""
    print("=" * 45)
    print("         AUTOMATIC REPORT GENERATOR")
    print("=" * 45)

    loaded_file = []
    file_name = ""

    while True:
        file_name = input("\nEnter the CSV file name to load: ").strip()
        if not file_name:
            print("File name cannot be empty. Please try again.")
            continue

        try:
            loaded_file = load_csv_file(file_name)
            print(f"Successfully loaded '{file_name}' with {len(loaded_file)} records.")
            break
        except ReportGeneratorError as err:
            print(f"Error: {err}")
            print("Please check the filename and try again.\n")

    print("\nActions:")
    print("  load   -> Load a new CSV file")
    print("  view   -> View CSV data preview")
    print("  report -> Generate financial/sales report")
    print("  exit   -> Exit program")
    print("-" * 45)

    while True:
        try:
            action = input("\nWhat action would you like to perform? > ").strip().lower()

            if not action:
                continue

            if action in ("exit", "quit"):
                print("Exiting Automatic Report Generator. Goodbye!")
                break

            valid_actions = ("load", "view", "report")

            if action not in valid_actions:
                raise InvalidInputError(
                    "Invalid action. Choose load, view, report, or exit."
                )

            loaded_file = process_report_action(file_name, loaded_file, action)

        except ReportGeneratorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    automatic_csv_report_generator()