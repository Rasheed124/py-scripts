from decimal import Decimal
from online_store import BusinessCustomer, Customer, PremiumCustomer, User

def show_price_summary(customer: Customer) -> None:
    amounts = customer.cal_final_price()
    print(f"\n{customer.customer_type} price summary")
    print(f"Subtotal: ₦{amounts['subtotal']:,.2f}")
    print(f"Discount: ₦{amounts['discount']:,.2f}")
    print(f"VAT:      ₦{amounts['vat']:,.2f}")
    print(f"Total:    ₦{amounts['total']:,.2f}")

def main() -> None:
    standard = Customer("John Doe", "john@example.com")
    premium = PremiumCustomer("Mary Jane", "mary@example.com")
    business = BusinessCustomer("Ada Okafor", "ada@company.example",
                                "ABC Office Supplies Ltd", "RC-123456")

    print(standard.display_user_information())
    print(premium.display_user_information())
    print(business.display_user_information())

    standard.add_product("Laptop", 1, Decimal("3500.00"))
    standard.add_product("Mouse", 2, Decimal("300.00"))
    premium.add_product("Phone", 1, Decimal("5000.00"))
    business.add_product("Office Chairs", 2, Decimal("6000.00"))

    print(standard.display_cart())
    for customer in (standard, premium, business):
        show_price_summary(customer)

    transaction = standard.checkout()
    print("\nCompleted transaction:", transaction)
    print(standard.display_transaction_history())

    print("\nInheritance checks")
    print("Premium is a Customer:", isinstance(premium, Customer))
    print("Business is a User:", isinstance(business, User))
    print("PremiumCustomer subclasses Customer:", issubclass(PremiumCustomer, Customer))

    print("\nValidation checks")
    for bad_price in (0, -10, True, float("inf"), float("nan")):
        try:
            standard.add_product("Invalid Item", 1, bad_price)
        except (TypeError, ValueError) as error:
            print(f"Rejected price {bad_price!r}: {error}")

    try:
        standard.add_product("Invalid Quantity", True, 100)
    except (TypeError, ValueError) as error:
        print(f"Rejected quantity: {error}")

    standard.deactivate_account()
    try:
        standard.add_product("Another Item", 1, 100)
    except PermissionError as error:
        print(f"Deactivated account blocked: {error}")

if __name__ == "__main__":
    main()
