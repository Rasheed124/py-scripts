# Problem 25 — Restaurant Ordering System

Run from this folder with `python main.py`.

Modules:
- `menu_item.py`: menu item identity, name, and price
- `order_item.py`: a menu item plus quantity and line total
- `order.py`: manages items, subtotal, discount, total, and receipt
- `customer.py`: customer details
- `validators.py`: reusable input validation

Rules: prices must be positive, quantities must be positive integers, and orders receive a 10% discount at subtotals of ₦20,000 or more. Totals are computed from current order items.
