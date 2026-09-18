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
ALLOWED_NAMES = {"sqrt", "log", "sin", "cos", "tan", "pi", "e"}

# Safe namespace provided to eval()
SAFE_MATH_GLOBALS = {
    "__builtins__": None,
    "sqrt": math.sqrt,
    "log": math.log,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
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
        # Pass SAFE_MATH_GLOBALS as the globals dict into eval()
        result = eval(sanitized_expression, SAFE_MATH_GLOBALS, {})
        return float(result)
    except ZeroDivisionError:
        raise MathDomainError("Cannot divide by zero.")
    except ValueError as val_err:
        # Handles domain errors like sqrt(-1) or log(0)
        raise MathDomainError(f"Math domain error: {val_err}")
    except Exception as exc:
        raise InvalidExpressionError(f"Syntax error in expression: {exc}")


if __name__ == "__main__":
    test_expressions = [
        "205 + 50 / 2 - (12 * 14)",
        "sqrt(16) + sin(pi / 2)",
        "log(e)",
        "sqrt(-1)",
        "25 + os.system",
    ]

    for expr in test_expressions:
        try:
            res = evaluate_expression(expr)
            print(f"SUCCESS: '{expr}' = {res}")
        except CalculatorError as err:
            print(f"FAILED:  '{expr}' -> Error: {err}")