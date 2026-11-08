from decimal import Decimal
from restaurant import Customer, MenuItem, Order, OrderItem

def main() -> None:
    burger = MenuItem("M001", "Chicken Burger", Decimal("5000.00"))
    pizza = MenuItem("M002", "Large Pizza", Decimal("12000.00"))
    juice = MenuItem("M003", "Fresh Juice", Decimal("1500.00"))

    customer = Customer("C001", "Alice Johnson", "alice@example.com")
    order = Order(customer)
    order.add_item(OrderItem(burger, 2))
    order.add_item(OrderItem(pizza, 1))
    order.add_item(OrderItem(juice, 2))

    print("=== INITIAL ORDER ===")
    print(order.generate_receipt())

    order.update_quantity("M001", 3)
    print("\n=== AFTER UPDATING BURGER QUANTITY ===")
    print(order.generate_receipt())

    order.remove_item("M003")
    print("\n=== AFTER REMOVING JUICE ===")
    print(order.generate_receipt())

    second_customer = Customer("C002", "David Smith", "david@example.com")
    second_order = Order(second_customer)
    second_order.add_item(OrderItem(juice, 4))
    print("\n=== SECOND CUSTOMER ORDER ===")
    print(second_order.generate_receipt())

    try:
        order.remove_item("M999")
    except KeyError as error:
        print("\nMissing item handled:", error)

    try:
        OrderItem(burger, 0)
    except ValueError as error:
        print("Invalid quantity handled:", error)

if __name__ == "__main__":
    main()
