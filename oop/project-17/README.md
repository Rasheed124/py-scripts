# Online Store Users — Problem 17

## Structure

```text
online_store_project/
├── main.py
├── README.md
└── online_store/
    ├── __init__.py
    ├── models.py
    ├── validators.py
    ├── user.py
    ├── customer.py
    ├── premium_customer.py
    └── business_customer.py
```

## Run

Open a terminal in this folder and run:

```bash
python main.py
```

No third-party packages are needed.

## Module responsibilities

- `models.py`: immutable Product and Transaction data classes.
- `validators.py`: shared input validation.
- `user.py`: shared account identity and activation status.
- `customer.py`: cart, checkout, pricing, and standard discount.
- `premium_customer.py`: premium membership and discount.
- `business_customer.py`: business details and bulk discount.
- `__init__.py`: convenient package imports.
- `main.py`: runnable demo and basic validation checks.

Example import:

```python
from online_store import Customer, PremiumCustomer, BusinessCustomer
```
