
# import json

# from pathlib import Path
# import csv


# class ExpenseTrackerError(Exception):
#     """Base exception for Expense Tracker domain errors."""
#     pass


# class InvalidInputError(ExpenseTrackerError):
#     """Raised when user input is invalid."""
#     pass


# class CvFileNotFoundError(ExpenseTrackerError):
#     """Raised when an Expense ID does not exist."""
#     pass


# class StorageError(ExpenseTrackerError):
#     """Raised when loading or saving JSON data fails."""
#     pass









# DATA_DIR = Path(__file__).parent


# def load_cv_file(filename: str) -> dict:
#     """Load data from a JSON file if it exists."""

#     data_file = (DATA_DIR / filename).with_suffix(".csv")


#     if not data_file.is_file():
#         raise StorageError(f"Data file not found: {filename}")

#     try:
#         with open(data_file, "r", encoding="utf-8", newline="") as f:
#             return list(csv.DictReader(f))
#     except (OSError, json.JSONDecodeError) as err:
#         raise StorageError(
#             f"Failed to load data from '{filename}': {err}"
#         ) from err



# def process_file_cleaner_action(file_name : str, loaded_file: dict, action: str) -> dict:
#     """Perform CRUD and aggregation operations on the expense dictionary."""

#     if  action == "load":
#         loaded_file = load_cv_file(file_name)
#         print(f"{'ID':<8} {'Customer Name':<22} {'City':<18} {'Status':<12}")
#         print("-" * 65)

#         for row in loaded_file:
#             print(
#                 f"{row['customer_id']:<8} "
#                 f"{row['customer_name']:<22} "
#                 f"{row['email']:<22} "
#                 f"{row['city']:<18} "
#                 f"{row['age']:<18} "
#                 f"{row['gender']:<18} "
#                 f"{row['order_date']:<12}"
#                 f"{row['product']:<12}"
#                 f"{row['quantity']:<12}"
#                 f"{row['unit_price']:<12}"
#                 f"{row['status']:<18} "
#             )


#     if  action == "missing":

#         required_columns = [
#             "customer_id",
#             "customer_name",
#             "email",
#             "city",
#             "age",
#             "gender",
#             "order_date",
#             "product",
#             "quantity",
#             "unit_price",
#             "status"
#         ]

#         loaded_file = load_cv_file(file_name)
#         if not loaded_file:
#             raise CvFileNotFoundError("The files is empty")

        
#         actual_columns = list(loaded_file[0].keys())

#         missing_columns = [
#             column for column in required_columns
#             if column not in actual_columns
#         ]

#         if missing_columns:
#             print("Missing columns:", missing_columns)
#         else:
#             print("All required columns are present.")


#     return loaded_file


# def expense_tracker_generator() -> None:
#     """Run the main CSV Data Cleaner CLI loop."""

#     while True:
#         file_name = input("Enter the CSV file name: ").strip()

#         if not file_name:
#             print("File name cannot be empty. Please try again.")
#             continue

#         try:
#             loaded_cv_file = load_cv_file(file_name)
#             break
#         except ExpenseTrackerError as err:
#             print(f"Storage Initialization Error: {err}")
#             print("Please try again.\n")

#     print("=" * 45)
#     print("              CSV DATA CLEANER")
#     print("=" * 45)
#     print("Actions:")
#     print("  load    -> Load a CSV file")
#     print("  view    -> View CSV data")
#     print("  clean   -> Clean messy data")
#     print("  validate-> Validate data")
#     print("  missing -> Check missing values")
#     print("  save    -> Save cleaned data")
#     print("  exit    -> Exit program")
#     print("-" * 45)

#     while True:
#         try:
#             action = input(
#                 "\nWhat action would you like to perform? > "
#             ).strip().lower()

#             if not action:
#                 continue

#             if action in ("exit", "quit"):
#                 print("Exiting CSV Data Cleaner. Goodbye!")
#                 break

#             valid_actions = ("load", "view", "clean", "validate", "missing", "save")

#             if action not in valid_actions:
#                 raise InvalidInputError(
#                     "Invalid action. Choose load, view, clean, validate, "
#                     "missing, save, or exit."
#                 )

#             loaded_cv_file = process_file_cleaner_action(
#                file_name, loaded_cv_file, action, 
#             )

#         except ExpenseTrackerError as err:
#             print(f"Error: {err}")

#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break

# if __name__ == "__main__":
#     expense_tracker_generator()

























import csv
from pathlib import Path


class CsvCleanerError(Exception):
    """Base exception for CSV Data Cleaner domain errors."""
    pass


class InvalidInputError(CsvCleanerError):
    """Raised when user input is invalid."""
    pass


class CsvFileNotFoundError(CsvCleanerError):
    """Raised when a CSV file does not exist or is empty."""
    pass


class StorageError(CsvCleanerError):
    """Raised when loading or saving CSV data fails."""
    pass


DATA_DIR = Path(__file__).parent


from datetime import datetime


def parse_and_format_date(date_str: str) -> str:
    """Try parsing date string across common formats and standardize to YYYY-MM-DD.
    Returns empty string if invalid or 'not available'."""


    date_str = date_str.strip()
    if not date_str or date_str.lower() in ("not available", "n/a", "none", "null"):
        return ""
    
    formats = [
        "%Y-%m-%d", 
        "%m/%d/%Y",  
        "%d/%m/%Y",  
        "%Y/%m/%d", 
        "%d-%m-%Y",  
    ]
    
    for fmt in formats:
        try:
            parsed_date = datetime.strptime(date_str, fmt)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            continue
            
    return ""


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
    except Exception as err:
        raise StorageError(f"Failed to load CSV file '{data_file.name}': {err}") from err


def save_csv_file(filename: str, data: list[dict]) -> None:
    """Save a list of dictionaries back into a CSV file using DictWriter."""
    if not data:
        raise InvalidInputError("No data available to save.")

    clean_name = filename.strip()
    data_file = DATA_DIR / clean_name
    if not data_file.suffix:
        data_file = data_file.with_suffix(".csv")

    try:
        with open(data_file, "w", encoding="utf-8", newline="") as f:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data successfully saved to {data_file.name}!")
    except Exception as err:
        raise StorageError(f"Failed to save CSV file: {err}") from err


def process_file_cleaner_action(file_name: str, loaded_file: list[dict], action: str) -> list[dict]:
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

    elif action == "clean":
        print("\n--- Cleaning Dataset (Standardizing Gender & Dates) ---")
        cleaned_rows_count = 0
        fields_modified_count = 0

        for row in loaded_file:
            row_modified = False

            for key, val in row.items():
                if isinstance(val, str):
                    row[key] = val.strip()

            if "gender" in row:
                g_val = row["gender"].lower()
                if g_val in ("f", "female"):
                    if row["gender"] != "Female":
                        row["gender"] = "Female"
                        fields_modified_count += 1
                        row_modified = True
                elif g_val in ("m", "male"):
                    if row["gender"] != "Male":
                        row["gender"] = "Male"
                        fields_modified_count += 1
                        row_modified = True
                else:
                    if row["gender"] != "":
                        row["gender"] = ""
                        fields_modified_count += 1
                        row_modified = True

            if "order_date" in row:
                original_date = row["order_date"]
                formatted_date = parse_and_format_date(original_date)
                if original_date != formatted_date:
                    row["order_date"] = formatted_date
                    fields_modified_count += 1
                    row_modified = True

            if "age" in row and row["age"]:
                try:
                    int(row["age"])
                except ValueError:
                    row["age"] = ""
                    fields_modified_count += 1
                    row_modified = True

            if "quantity" in row and row["quantity"]:
                try:
                    int(row["quantity"])
                except ValueError:
                    row["quantity"] = ""
                    fields_modified_count += 1
                    row_modified = True

            if "unit_price" in row and row["unit_price"]:
                try:
                    float(row["unit_price"])
                except ValueError:
                    row["unit_price"] = ""
                    fields_modified_count += 1
                    row_modified = True

            if row_modified:
                cleaned_rows_count += 1

        print(f"Cleaning complete! Standardized/cleared {fields_modified_count} field(s) across {cleaned_rows_count} row(s).")

    elif action == "validate":
        print("\n--- Validating Dataset Domain Rules ---")
        errors_found = 0

        for idx, row in enumerate(loaded_file, start=1):

            if "gender" in row and row["gender"]:
                if row["gender"].lower() not in ("female", "male", "f", "m", "unknown"):
                    print(f"Row {idx} [gender]: Unrecognized value '{row['gender']}'")
                    errors_found += 1

            if "order_date" in row and row["order_date"]:
                if parse_and_format_date(row["order_date"]) == "":
                    print(f"Row {idx} [order_date]: Invalid or non-standard date '{row['order_date']}'")
                    errors_found += 1

        if errors_found == 0:
            print("Validation complete: All records comply with domain expectations!")
        else:
            print(f"Validation complete: Found {errors_found} issue(s). Run 'clean' to automatically fix them.")

    elif action == "missing":
        required_columns = [
            "customer_id", "customer_name", "email", "city", 
            "age", "gender", "order_date", "product", "quantity", "unit_price", "status"
        ]
        
        actual_columns = list(loaded_file[0].keys())
        missing_columns = [col for col in required_columns if col not in actual_columns]

        print("\n--- Column & Missing Value Audit ---")
        if missing_columns:
            print(f"Missing required columns: {missing_columns}")
        else:
            print("All required columns are present.")

        empty_cells = 0
        for row_idx, row in enumerate(loaded_file, start=1):
            for col, val in row.items():
                if not val or not str(val).strip():
                    empty_cells += 1

        print(f"Found {empty_cells} empty cell(s) across the dataset.")

    elif action == "save":
        out_name = input("Enter output filename (e.g., cleaned_data.csv): ").strip()
        if not out_name:
            out_name = "cleaned_data.csv"
        save_csv_file(out_name, loaded_file)

    return loaded_file

def csv_cleaner_generator() -> None:
    """Run the main CSV Data Cleaner CLI loop."""
    print("=" * 45)
    print("                 CSV DATA CLEANER")
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
        except CsvCleanerError as err:
            print(f"Error: {err}")
            print("Please check the filename and try again.\n")

    print("\nActions:")
    print("  load     -> Load a CSV file")
    print("  view     -> View CSV data preview")
    print("  clean    -> Clean whitespace from data")
    print("  validate -> Validate numerical fields")
    print("  missing  -> Check for missing columns and values")
    print("  save     -> Save cleaned data to a new file")
    print("  exit     -> Exit program")
    print("-" * 45)

    while True:
        try:
            action = input("\nWhat action would you like to perform? > ").strip().lower()

            if not action:
                continue

            if action in ("exit", "quit"):
                print("Exiting CSV Data Cleaner. Goodbye!")
                break

            valid_actions = ("load", "view", "clean", "validate", "missing", "save")

            if action not in valid_actions:
                raise InvalidInputError(
                    "Invalid action. Choose load, view, clean, validate, missing, save, or exit."
                )

            loaded_file = process_file_cleaner_action(file_name, loaded_file, action)

        except CsvCleanerError as err:
            print(f"Error: {err}")
        except ( KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    csv_cleaner_generator()











































#     import csv
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
#     """Perform universal actions on any loaded CSV dataset dynamically."""

#     if action == "load":
#         loaded_file = load_csv_file(file_name)
#         print(f"\nSuccessfully reloaded {len(loaded_file)} row(s) from '{file_name}'.")

#     elif action == "view":
#         if not loaded_file:
#             print("\nNo data currently loaded.")
#             return loaded_file

#         print(f"\n--- Previewing Dataset ({len(loaded_file)} total rows) ---")
        
#         # Dynamically grab headers directly from the first row dictionary keys
#         headers = list(loaded_file[0].keys())
#         header_str = " | ".join(f"{h:<18}" for h in headers)
#         print(header_str)
#         print("-" * len(header_str))

#         # Print first 10 rows dynamically
#         for row in loaded_file[:10]:
#             row_str = " | ".join(f"{str(row.get(h, '')):<18}" for h in headers)
#             print(row_str)
#         if len(loaded_file) > 10:
#             print(f"... and {len(loaded_file) - 10} more rows.")

#     elif action == "clean":
#         print("\n--- Cleaning Dataset (Stripping Whitespace) ---")
#         cleaned_count = 0
#         for row in loaded_file:
#             for key, val in row.items():
#                 if isinstance(val, str):
#                     row[key] = val.strip()
#             cleaned_count += 1
#         print(f"Cleaned whitespace across {cleaned_count} row(s).")

#     elif action == "validate":
#         print("\n--- Universal Data Type Inspection ---")
#         # Dynamically inspect columns and report what data types they hold
#         headers = list(loaded_file[0].keys())
#         print(f"Inspecting {len(headers)} columns across {len(loaded_file)} rows...")

#         for header in headers:
#             numeric_count = 0
#             text_count = 0
#             empty_count = 0

#             for row in loaded_file:
#                 val = row.get(header, "").strip()
#                 if not val:
#                     empty_count += 1
#                     continue
                
#                 # Check if value can be interpreted as a number
#                 try:
#                     float(val)
#                     numeric_count += 1
#                 except ValueError:
#                     text_count += 1

#             print(f"  • Column '{header}': {numeric_count} numeric, {text_count} text, {empty_count} empty values.")

#     elif action == "missing":
#         headers = list(loaded_file[0].keys())
#         print(f"\n--- Dynamic Missing Value Audit ---")
#         print(f"Detected Headers: {', '.join(headers)}")

#         empty_cells = 0
#         rows_with_missing = 0

#         for row_idx, row in enumerate(loaded_file, start=1):
#             row_has_empty = False
#             for col, val in row.items():
#                 if not val or not str(val).strip():
#                     empty_cells += 1
#                     row_has_empty = True
#             if row_has_empty:
#                 rows_with_missing += 1

#         print(f"Audit Results:")
#         print(f"  • Total rows evaluated: {len(loaded_file)}")
#         print(f"  • Rows containing empty cells: {rows_with_missing}")
#         print(f"  • Total empty cells found: {empty_cells}")

#     elif action == "save":
#         out_name = input("Enter output filename (e.g., cleaned_data.csv): ").strip()
#         if not out_name:
#             out_name = "cleaned_data.csv"
#         save_csv_file(out_name, loaded_file)

#     return loaded_file


# def csv_cleaner_generator() -> None:
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
#     print("  validate -> Inspect data types per column")
#     print("  missing  -> Audit missing values dynamically")
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

#             valid_actions = ("load", "view", "clean", "validate", "missing", "save")

#             if action not in valid_actions:
#                 raise InvalidInputError(
#                     "Invalid action. Choose load, view, clean, validate, missing, save, or exit."
#                 )

#             loaded_file = process_file_cleaner_action(file_name, loaded_file, action)

#         except CsvCleanerError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     csv_cleaner_generator()