class CalculatorError(Exception):
    pass


class InvalidCalculationError(CalculatorError):
    pass


class InvalidOperatorError(CalculatorError):
    pass


class InvalidInputError(CalculatorError):
    pass



operators = {"+", "-", "*", "/", "//", "%", "**", "(" , ")"}
digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def calculator(): 
    user_input = input("Calc : ").strip().replace(" ", "")

    for char in user_input:
        if char not in operators and char not in digits:
            raise InvalidOperatorError("Invalid operator")

    evaluate = eval(user_input)
    print(evaluate)

while True:
    try:
        calculator()
    except CalculatorError as e:
        print(e)
        continue

