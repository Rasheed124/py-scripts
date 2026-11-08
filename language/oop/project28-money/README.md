# Project 28 — Custom Money Class

## Run

Open a terminal in this project folder and run:

```powershell
python main.py
```

## Structure

- `main.py`: operator and validation demonstrations.
- `money/__init__.py`: package exports.
- `money/money.py`: `Money` class and dunder methods.
- `money/validators.py`: amount and currency validation.

## Behavior choices

- Amounts are stored as `Decimal`; negative amounts are allowed.
- Currency codes are normalized to uppercase and must be three letters.
- Addition, subtraction, and ordering comparisons require matching currencies.
- Equality compares both amount and currency. Equal numeric amounts in different currencies are not equal.
- `__str__` is user-readable; `__repr__` is developer-oriented.
