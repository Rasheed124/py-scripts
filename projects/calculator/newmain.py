import math
import re


class CalculatorError(Exception):
    """Base exception for all calculator errors."""

    pass


class InvalidExpressionError(CalculatorError):
    """Raised when an expression has invalid syntax or forbidden characters."""

    pass


class MathDomainError(CalculatorError):
    """Raised for mathematical errors like division by zero or invalid roots."""

    pass


# Allowed single characters (including letters for function names)
ALLOWED_CHARACTERS = set("0123456789+-*/(). abcdefghijklmnopqrstuvwxyz_")

# Strict whitelist of allowed functions and constants
ALLOWED_NAMES = {
    "sqrt",
    "log",
    "sin",
    "cos",
    "tan",
    "radians",
    "degrees",
    "pi",
    "e",
}

# Safe namespace provided to eval()
SAFE_MATH_GLOBALS = {
    "__builtins__": None,
    "sqrt": math.sqrt,
    "log": math.log,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "radians": math.radians,
    "degrees": math.degrees,
    "pi": math.pi,
    "e": math.e,
}


def validate_expression(expression: str) -> None:
    """Validates that the expression contains only allowed characters and whitelisted math functions."""
    if not expression.strip():
        raise InvalidExpressionError("Expression cannot be empty.")

    # 1. Validate individual characters
    invalid_chars = set(expression.lower()) - ALLOWED_CHARACTERS
    if invalid_chars:
        chars_list = ", ".join(sorted(invalid_chars))
        raise InvalidExpressionError(f"Invalid character(s) found: {chars_list}")

    # 2. Extract all letter words and check against the whitelist
    words = set(re.findall(r"[a-zA-Z_]\w*", expression))
    disallowed_words = words - ALLOWED_NAMES
    if disallowed_words:
        words_list = ", ".join(sorted(disallowed_words))
        raise InvalidExpressionError(f"Forbidden word(s) found: {words_list}")


def evaluate_expression(expression: str) -> float:
    """Evaluates an arithmetic string with advanced math extensions safely."""
    sanitized_expression = expression.strip()
    validate_expression(sanitized_expression)

    try:
        result = eval(sanitized_expression, SAFE_MATH_GLOBALS, {})
        return float(result)
    except ZeroDivisionError:
        raise MathDomainError("Cannot divide by zero.")
    except ValueError as val_err:
        raise MathDomainError(f"Math domain error: {val_err}")
    except Exception as exc:
        raise InvalidExpressionError(f"Syntax error in expression: {exc}")


def run_cli() -> None:
    """Runs the interactive command-line interface loop for the calculator."""
    last_result: float | None = None

    print("=" * 50)
    print("           SAFE PYTHON CALCULATOR ENGINE")
    print("=" * 50)
    print("Commands:")
    print("  'exit' or 'quit' -> Close calculator")
    print("  'C'              -> Clear current expression buffer / reset")
    print("  'DEL'            -> Remove last entered character from previous string")
    print("  'ans'            -> Reference the result of the previous calculation")
    print("-" * 50)

    raw_buffer = ""

    while True:
        try:
            user_input = input("\ncalc > ").strip()

            if user_input.lower() in ("exit", "quit"):
                print("Exiting calculator. Goodbye!")
                break

            if user_input.upper() == "C":
                raw_buffer = ""
                last_result = None
                print("[Clearing state and memory buffer...]")
                continue

            if user_input.upper() == "DEL":
                if raw_buffer:
                    raw_buffer = raw_buffer[:-1]
                    print(f"[Deleted last char. Current buffer: '{raw_buffer}']")
                else:
                    print("[Buffer is already empty!]")
                continue

            raw_buffer = user_input


            working_expression = raw_buffer
            if "ans" in working_expression.lower():
                if last_result is None:
                    raise InvalidExpressionError(
                        "No previous result available in memory ('ans')."
                    )
                working_expression = re.sub(
                    r"\bans\b", str(last_result), working_expression, flags=re.IGNORECASE
                )

            result = evaluate_expression(working_expression)
            last_result = result
            print(f"= {result}")

        except CalculatorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_cli()