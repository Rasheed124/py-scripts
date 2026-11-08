# Project 30 — Complete E-Commerce Management System

## Run
Requires Python 3.10+. No third-party packages needed.

```powershell
python main.py
```

## Structure
- `users/`: User, Customer, Admin
- `products/`: Product and inventory
- `cart/`: CartItem and ShoppingCart
- `orders/`: Order snapshots and statuses
- `payments/`: abstract PaymentProcessor, simulated card and bank transfer
- `notifications/`: abstract Notifier, email/SMS and duck-typed push
- `services/`: Store coordinating registration, products, checkout and notifications
- `validators.py`: reusable validation

## Rules
- 10% discount when subtotal is at least ₦100,000.
- Money uses `Decimal`.
- Stock and cart remain unchanged when simulated payment fails.
- Successful orders are recorded in customer history; notifications follow successful checkout.
- This is an in-memory learning project. Payments are simulated; never enter real payment credentials.
- Real production checkout needs a payment provider, persistent storage, and transaction/locking safeguards.
