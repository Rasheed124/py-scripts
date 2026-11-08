# Project 27 — Class and Static Methods: Object Factory

## Run the project

From this directory, run:

```powershell
python main.py
```

## String formats

- Product: `name,price,quantity` (example: `Laptop,850000,5`)
- ElectronicsProduct: `name,price,quantity,warranty_months` (example: `Tablet,300000,4,12`)

## Concepts demonstrated

- Normal construction with `__init__`
- Alternative constructors with `@classmethod`
- Utility validation with `@staticmethod`
- Inheritance-aware construction using `cls(...)`
- An instance method that uses object state
- Input validation and `Decimal` for price calculations

## Method differences

- `@classmethod` receives the class as `cls`, so it can construct the class on which it is called.
- `@staticmethod` receives neither `self` nor `cls`; it is useful for a related utility that needs no object or class state.
- An instance method receives `self` and can use that particular product's price and quantity.
