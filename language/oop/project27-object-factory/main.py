from decimal import Decimal
from products import Product, ElectronicsProduct


def main():
    print("=== Product Object Factory ===")

    laptop = Product("Laptop", Decimal("850000"), 5)
    print("\nNormal construction:")
    print(laptop)
    print("Stock value:", laptop.calculate_stock_value())

    mouse = Product.from_dict({
        "name": "Mouse",
        "price": "12500.50",
        "quantity": 20,
    })
    print("\nFrom dictionary:")
    print(mouse)
    print("Type:", type(mouse).__name__)

    keyboard = Product.from_string("Keyboard,25000,12")
    print("\nFrom string:")
    print(keyboard)

    print("\nStatic method:")
    print("Is 1500 valid?", Product.is_valid_price(1500))
    print("Is -20 valid?", Product.is_valid_price(-20))
    print("Is 'hello' valid?", Product.is_valid_price("hello"))

    phone = ElectronicsProduct.from_dict({
        "name": "Smartphone",
        "price": "450000",
        "quantity": 8,
        "warranty_months": 24,
    })
    tablet = ElectronicsProduct.from_string("Tablet,300000,4,12")
    print("\nSubclass constructors:")
    print(phone)
    print("Type:", type(phone).__name__)
    print(tablet)
    print("Type:", type(tablet).__name__)
    print("Phone stock value:", phone.calculate_stock_value())

    print("\nInvalid input examples:")
    invalid_inputs = [
        lambda: Product.from_dict({"name": "Mouse", "price": 100}),
        lambda: Product.from_string("Laptop,850000"),
        lambda: Product("Monitor", -100, 3),
    ]
    for action in invalid_inputs:
        try:
            action()
        except (TypeError, ValueError) as error:
            print(f"Handled {type(error).__name__}: {error}")


if __name__ == "__main__":
    main()
