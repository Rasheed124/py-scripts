

# class ConverterError(Exception):
#     """Base exception class for Converter domain errors."""
#     pass
# class InvalidFromUnitError(ConverterError):
#     """Raised when the source unit is invalid."""
#     pass
# class InvalidToUnitError(ConverterError):
#     """Raised when the target unit is invalid."""
#     pass

# conversion_terms_unit = {
#     # Length
#     ("km", "m"): lambda value: value * 1000,
#     ("m", "km"): lambda value: value / 1000,
#     ("m", "cm"): lambda value: value * 100,
#     ("cm", "m"): lambda value: value / 100,
#     ("cm", "mm"): lambda value: value * 10,
#     ("mm", "cm"): lambda value: value / 10,
#     ("km", "mi"): lambda value: value * 0.621371,
#     ("mi", "km"): lambda value: value / 0.621371,
#     ("mi", "ft"): lambda value: value * 5280,
#     ("ft", "mi"): lambda value: value / 5280,
#     ("ft", "in"): lambda value: value * 12,
#     ("in", "ft"): lambda value: value / 12,

#     # Weight
#     ("kg", "g"): lambda value: value * 1000,
#     ("g", "kg"): lambda value: value / 1000,
#     ("g", "mg"): lambda value: value * 1000,
#     ("mg", "g"): lambda value: value / 1000,
#     ("kg", "lb"): lambda value: value * 2.20462,
#     ("lb", "kg"): lambda value: value / 2.20462,
#     ("lb", "oz"): lambda value: value * 16,
#     ("oz", "lb"): lambda value: value / 16,

#     # Temperature
#     ("C", "F"): lambda value: (value * 9 / 5) + 32,
#     ("F", "C"): lambda value: (value - 32) * 5 / 9,
#     ("C", "K"): lambda value: value + 273.15,
#     ("K", "C"): lambda value: value - 273.15,

#     # Time
#     ("s", "min"): lambda value: value / 60,
#     ("min", "s"): lambda value: value * 60,
#     ("min", "h"): lambda value: value / 60,
#     ("h", "min"): lambda value: value * 60,
#     ("h", "day"): lambda value: value / 24,
#     ("day", "h"): lambda value: value * 24,
# }


# def conversion_calc(user_input) -> float:

#     user_from_unit = input("Input your unit: ").strip().replace(" ", "")

#     if user_from_unit not in {unit for pair in conversion_terms_unit for unit in pair}:
#         raise InvalidFromUnitError("Invalid starting unit")
    
#     user_to_unit = input("Input unit where you are converting to: ").strip().replace(" ", "")
#     if user_to_unit not in {unit for pair in conversion_terms_unit for unit in pair}:
#         raise InvalidToUnitError("Invalid target unit")
    
#     conversion = conversion_terms_unit[(user_from_unit, user_to_unit)]
#     result = conversion(user_input)
#     return result


# def run_coverter() -> None:

#     print("=" * 45)
#     print("        PYTHON UNIT CONVERTER")
#     print("=" * 45)
#     print("Categories:")
#     print("  Length       -> km, m, cm, mm, mi, ft, in")
#     print("  Weight       -> kg, g, mg, lb, oz")
#     print("  Temperature  -> C, F, K")
#     print("  Time         -> s, min, h, day")
#     print("-" * 45)

#     while True:
#         try:
#             user_value = float(input("Input your value: ").strip().replace(" ", ""))

#             conversion_result = conversion_calc(user_value)
#             print(conversion_result)

#         except ValueError:
#             print("Value must be a number.")
#             continue

#         except ConverterError as err:
#             print(f"Error: {err}")
#         except (KeyboardInterrupt, EOFError):
#             print("\nSession interrupted. Goodbye!")
#             break


# if __name__ == "__main__":
#     run_coverter()






# =============================== AI AFTER REVIEW





import re


class ConverterError(Exception):
    """Base exception class for Converter domain errors."""
    pass


class InvalidUnitError(ConverterError):
    """Raised when source or target units are invalid or missing."""
    pass


class IncompatibleConversionError(ConverterError):
    """Raised when conversion between two units is not supported."""
    pass


# Map of explicit unit pairs to conversion functions
CONVERSION_TERMS = {
    # Length
    ("km", "m"): lambda v: v * 1000,
    ("m", "km"): lambda v: v / 1000,
    ("m", "cm"): lambda v: v * 100,
    ("cm", "m"): lambda v: v / 100,
    ("cm", "mm"): lambda v: v * 10,
    ("mm", "cm"): lambda v: v / 10,
    ("km", "mi"): lambda v: v * 0.621371,
    ("mi", "km"): lambda v: v / 0.621371,
    ("mi", "ft"): lambda v: v * 5280,
    ("ft", "mi"): lambda v: v / 5280,
    ("ft", "in"): lambda v: v * 12,
    ("in", "ft"): lambda v: v / 12,

    # Weight
    ("kg", "g"): lambda v: v * 1000,
    ("g", "kg"): lambda v: v / 1000,
    ("g", "mg"): lambda v: v * 1000,
    ("mg", "g"): lambda v: v / 1000,
    ("kg", "lb"): lambda v: v * 2.20462,
    ("lb", "kg"): lambda v: v / 2.20462,
    ("lb", "oz"): lambda v: v * 16,
    ("oz", "lb"): lambda v: v / 16,

    # Temperature
    ("c", "f"): lambda v: (v * 9 / 5) + 32,
    ("f", "c"): lambda v: (v - 32) * 5 / 9,
    ("c", "k"): lambda v: v + 273.15,
    ("k", "c"): lambda v: v - 273.15,

    # Time
    ("s", "min"): lambda v: v / 60,
    ("min", "s"): lambda v: v * 60,
    ("min", "h"): lambda v: v / 60,
    ("h", "min"): lambda v: v * 60,
    ("h", "day"): lambda v: v / 24,
    ("day", "h"): lambda v: v * 24,
}


def parse_and_convert(user_input: str) -> str:
    """
    Parses single-line input like '100 km to mi' or '32 c to f'
    and executes the conversion calculation.
    """
    # Regex matching: <number> <from_unit> to <to_unit>
    pattern = r"^([+-]?\d+(?:\.\d+)?)\s*([a-zA-Z]+)\s+(?:to|in)\s+([a-zA-Z]+)$"
    match = re.match(pattern, user_input.strip(), re.IGNORECASE)

    if not match:
        raise InvalidUnitError(
            "Invalid format. Expected format: '<value> <from_unit> to <to_unit>' (e.g., '100 km to mi')"
        )

    val_str, from_unit, to_unit = match.groups()
    value = float(val_str)
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Self conversion shortcut
    if from_unit == to_unit:
        return f"{value} {to_unit}"

    pair = (from_unit, to_unit)

    if pair not in CONVERSION_TERMS:
        raise IncompatibleConversionError(
            f"Unsupported conversion from '{from_unit}' to '{to_unit}'."
        )

    result = CONVERSION_TERMS[pair](value)
    return f"{value} {from_unit} = {result:.4f} {to_unit}"


def run_converter() -> None:
    """Main CLI loop maintaining natural language converter interface."""
    print("=" * 45)
    print("         PYTHON UNIT CONVERTER CLI")
    print("=" * 45)
    print("Usage Example:")
    print("  '100 km to mi'")
    print("  '32 c to f'")
    print("  'exit' / 'quit' -> Exit program")
    print("-" * 45)

    while True:
        try:
            raw_input = input("convert > ").strip()

            if not raw_input:
                continue

            if raw_input.lower() in ("exit", "quit"):
                print("Exiting converter. Goodbye!")
                break

            output = parse_and_convert(raw_input)
            print(f"= {output}\n")

        except ConverterError as err:
            print(f"Error: {err}\n")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_converter()