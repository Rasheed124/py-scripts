import math
import re


class CalculatorError(Exception):
    """Base exception class for calculator domain errors."""
    pass


class InvalidInputError(CalculatorError):
    """Raised when input syntax or characters are invalid."""
    pass


class InvalidCalculationError(CalculatorError):
    """Raised when runtime math evaluation fails."""
    pass


SAFE_MATH_GLOBALS = {
    "__builtins__": {},  
    "sqrt": math.sqrt,
    "log": math.log,
    "log10": math.log10,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "pi": math.pi,
    "e": math.e,
}

BASE_CHARS = {"+", "-", "*", "/", "%", "(", ")", ".", ","} | {str(i) for i in range(10)}
FUNCTION_CHARS = {
    char
    for key in SAFE_MATH_GLOBALS.keys()
    if key != "__builtins__"
    for char in key
}
ALLOWED_CHARS = BASE_CHARS | FUNCTION_CHARS


def evaluate_expression(expr: str) -> float | int:
    """Validates individual characters and safely evaluates mathematical expressions."""
    clean_expr = expr.replace(" ", "").lower()

    if not clean_expr:
        raise InvalidInputError("Expression cannot be empty.")

    for char in clean_expr:
        if char not in ALLOWED_CHARS:
            raise InvalidInputError(f"Invalid character in expression: '{char}'")

    try:
        return eval(clean_expr, SAFE_MATH_GLOBALS, {})
    except ZeroDivisionError:
        raise InvalidCalculationError("Cannot divide by zero.")
    except ValueError as val_err:
        raise InvalidCalculationError(f"Math domain error: {val_err}")
    except SyntaxError:
        raise InvalidCalculationError("Invalid expression syntax.")
    except NameError as name_err:
        raise InvalidCalculationError(f"Unrecognized function or variable name: {name_err}")


def process_input(raw_input: str, last_result: float | int | None) -> str:
    """Handles system commands and transforms operators/keywords into executable math expressions."""
    if raw_input.lower() in ("exit", "quit"):
        return "EXIT"

    if raw_input.upper() == "C":
        return "CLEAR"

    working_expr = raw_input

    if working_expr[0] in "+-*/%":
        if last_result is None:
            raise InvalidInputError("No previous result available to continue calculation.")
        working_expr = f"{last_result}{working_expr}"

    if "ans" in working_expr.lower():
        if last_result is None:
            raise InvalidInputError("No previous result available in memory ('ans').")
        working_expr = re.sub(
            r"\bans\b", str(last_result), working_expr, flags=re.IGNORECASE
        )

    return working_expr


def run_calculator() -> None:
    """Main CLI loop maintaining state across iterations."""
    last_result: float | int | None = None

    print("=" * 45)
    print("      SCIENTIFIC PYTHON CALCULATOR ENGINE")
    print("=" * 45)
    print("Commands:")
    print("  'exit' / 'quit' -> Exit program")
    print("  'C'             -> Clear memory state")
    print("  'ans'           -> Use previous calculation result")
    print("  Functions       -> sqrt, log, log10, sin, cos, tan")
    print("  Constants       -> pi, e")
    print("-" * 45)

    while True:
        try:
            prompt_prefix = f"calc [{last_result}] > " if last_result is not None else "calc > "
            raw_input = input(prompt_prefix).strip()

            if not raw_input:
                continue

            action = process_input(raw_input, last_result)

            if action == "EXIT":
                print("Exiting calculator. Goodbye!")
                break
            elif action == "CLEAR":
                last_result = None
                print("[Memory cleared.]")
                continue

            result = evaluate_expression(action)
            last_result = result
            print(f"= {result}")

        except CalculatorError as err:
            print(f"Error: {err}")
        except (KeyboardInterrupt, EOFError):
            print("\nSession interrupted. Goodbye!")
            break


if __name__ == "__main__":
    run_calculator()