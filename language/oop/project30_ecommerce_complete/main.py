from cart.shopping_cart import ShoppingCart
from notifications.email_notifier import EmailNotifier
from notifications.push_notifier import PushNotifier
from notifications.sms_notifier import SMSNotifier
from payments.bank_transfer import BankTransferPayment
from payments.card_payment import CardPayment
from products.product import Product
from services.store import Store
from users.admin import Admin
from users.customer import Customer


def section(title):
    print("\n" + "=" * 10 + f" {title} " + "=" * 10)


def main():
    store = Store("RT Store")
    admin = Admin("Store Admin", "admin@example.com", "+2348098765432", "adminpass123")
    section("ADMIN")
    print(admin.get_details())

    customer = Customer(
        "Ada Okafor", "ada@example.com", "+2348012345678",
        "learning123", "Ikeja, Lagos, Nigeria",
    )
    store.register_customer(customer)
    laptop = store.add_product(Product("Laptop", "450000", 5, "Computers"))
    mouse = store.add_product(Product("Wireless Mouse", "12000", 20, "Accessories"))

    section("STORE")
    print(store)
    for product in store.products:
        print(product)

    customer.shopping_cart.add_item(laptop, 1)
    customer.shopping_cart.add_item(mouse, 2)
    section("CART")
    print(customer.shopping_cart)

    section("SUCCESSFUL CARD CHECKOUT")
    order = store.checkout(customer, CardPayment(should_succeed=True), EmailNotifier())
    print(order)
    print("Stock remaining:", laptop.stock, "laptops;", mouse.stock, "mice")
    print("Cart empty:", customer.shopping_cart.is_empty)
    print("Successful order history:", len(customer.order_history))

    section("FAILED BANK TRANSFER")
    customer.shopping_cart.add_item(mouse, 1)
    stock_before = mouse.stock
    failed = store.checkout(customer, BankTransferPayment(should_succeed=False))
    print(failed)
    print("Stock unchanged:", mouse.stock == stock_before)
    print("Cart preserved:", not customer.shopping_cart.is_empty)
    print("Successful order history remains:", len(customer.order_history))

    section("DUCK-TYPED PUSH NOTIFICATION")
    store.notify(customer, "Your cart is waiting for you.", PushNotifier())
    section("SMS NOTIFICATION")
    store.notify(customer, "A sample store message.", SMSNotifier())

    section("ORDER HISTORY")
    for saved_order in customer.order_history:
        print(saved_order.summary())

    section("FINAL SUMMARY")
    print("Products:", len(store))
    print("Customers:", len(store.customers))
    print("Orders recorded by store:", len(store.orders))
    print("Successful customer orders:", len(customer.order_history))


if __name__ == "__main__":
    main()
