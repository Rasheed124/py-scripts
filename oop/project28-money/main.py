from decimal import Decimal

from money import Money


def main():
    print("=== Custom Money Class ===")

    money1 = Money("2000.00", "ngn")
    money2 = Money("1500.50", "NGN")
    money3 = Money("2000.00", "USD")

    print("\nReadable string (__str__):")
    print(money1)

    print("\nDeveloper representation (__repr__):")
    print(repr(money1))

    # 2. Addition and subtraction
    print("\nArithmetic:")
    print("money1 + money2 =", money1 + money2)
    print("money1 - money2 =", money1 - money2)
    print("money2 - money1 =", money2 - money1)  # Negative amounts are allowed.

    # 3. Comparisons
    print("\nComparisons:")
    print("money1 > money2:", money1 > money2)
    print("money1 == Money('2000', 'NGN'):", money1 == Money("2000", "NGN"))
    print("money1 != money2:", money1 != money2)
    print("money1 <= money2:", money1 <= money2)
    print("money1 >= money2:", money1 >= money2)
    print("money2 < money1:", money2 < money1)

    # 4. Different currencies: equality is False; arithmetic/order comparisons raise.
    print("\nDifferent currencies:")
    print("NGN amount equals USD amount?", money1 == money3)
    try:
        print(money1 + money3)
    except ValueError as error:
        print("Addition handled:", error)

    try:
        print(money1 > money3)
    except ValueError as error:
        print("Ordering comparison handled:", error)

    # 5. Invalid input handling
    print("\nValidation:")
    invalid_inputs = [
        lambda: Money("not-a-number", "NGN"),
        lambda: Money("100", "  "),
        lambda: Money(True, "NGN"),
        lambda: Money("NaN", "NGN"),
    ]
    for action in invalid_inputs:
        try:
            action()
        except (TypeError, ValueError) as error:
            print(f"Handled {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
