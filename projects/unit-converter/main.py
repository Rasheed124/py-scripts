

# LENGTH_UNITS = {
#     "meter": 1.0,
#     "kilometer": 1000.0,
#     "centimeter": 0.01,
#     "millimeter": 0.001,
#     "mile": 1609.344,
#     "yard": 0.9144,
#     "foot": 0.3048,
#     "inch": 0.0254,
# }

# WEIGHT_UNITS = {
#     "gram": 1.0,
#     "kilogram": 1000.0,
#     "milligram": 0.001,
#     "pound": 453.59237,
#     "ounce": 28.349523125,
# }

# TEMPERATURE_UNITS = {
#     "celsius": {
#         "to_base": lambda c: c,
#         "from_base": lambda c: c,
#     },
#     "fahrenheit": {
#         "to_base": lambda f: (f - 32) * 5 / 9,
#         "from_base": lambda c: (c * 9 / 5) + 32,
#     },
#     "kelvin": {
#         "to_base": lambda k: k - 273.15,
#         "from_base": lambda c: c + 273.15,
#     },
# }

# CATEGORIES = {
#     "length": LENGTH_UNITS,
#     "weight": WEIGHT_UNITS,
# }


# def convert_linear(value: float, from_unit: str, to_unit: str, category: str) -> float:
#     """Converts a value between two units in a linear category using a base-unit standard."""
#     if category not in CATEGORIES:
#         raise ValueError(f"Unknown category: '{category}'")

#     unit_dict = CATEGORIES[category]
#     from_unit = from_unit.lower().strip()
#     to_unit = to_unit.lower().strip()

#     if from_unit not in unit_dict:
#         raise ValueError(f"Unknown unit '{from_unit}' in category '{category}'")
#     if to_unit not in unit_dict:
#         raise ValueError(f"Unknown unit '{to_unit}' in category '{category}'")

#     base_value = value * unit_dict[from_unit]
#     return base_value / unit_dict[to_unit]


# def convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
#     """Converts temperature values using functional transformation handlers."""
#     from_unit = from_unit.lower().strip()
#     to_unit = to_unit.lower().strip()

#     if from_unit not in TEMPERATURE_UNITS:
#         raise ValueError(f"Unknown temperature unit: '{from_unit}'")
#     if to_unit not in TEMPERATURE_UNITS:
#         raise ValueError(f"Unknown temperature unit: '{to_unit}'")

#     celsius_value = TEMPERATURE_UNITS[from_unit]["to_base"](value)
#     return TEMPERATURE_UNITS[to_unit]["from_base"](celsius_value)


# if __name__ == "__main__":
#     print("--- Stage 2 Temperature Conversion Tests ---")

#     # 100 Celsius to Fahrenheit
#     f_val = convert_temperature(100, "celsius", "fahrenheit")
#     print(f"100 Celsius = {f_val:.2f} Fahrenheit")

#     # 32 Fahrenheit to Celsius
#     c_val = convert_temperature(32, "fahrenheit", "celsius")
#     print(f"32 Fahrenheit = {c_val:.2f} Celsius")

#     # 0 Kelvin to Celsius
#     k_val = convert_temperature(0, "kelvin", "celsius")
#     print(f"0 Kelvin = {k_val:.2f} Celsius")





"""
Project 2: Unit Converter Engine (Stage 3)
Alias Normalization, Custom Exceptions, and Unified Routing
"""

class UnitConverterError(Exception):
    """Base exception for all unit converter errors."""
    pass

class UnknownCategoryError(UnitConverterError):
    """Raised when a requested category is not registered."""
    pass

class UnknownUnitError(UnitConverterError):
    """Raised when an input unit or alias cannot be resolved."""
    pass

class IncompatibleUnitsError(UnitConverterError):
    """Raised when attempting to convert between mismatched categories."""
    pass


LENGTH_UNITS = {
    "meter": 1.0,
    "kilometer": 1000.0,
    "centimeter": 0.01,
    "millimeter": 0.001,
    "mile": 1609.344,
    "yard": 0.9144,
    "foot": 0.3048,
    "inch": 0.0254,
}

WEIGHT_UNITS = {
    "gram": 1.0,
    "kilogram": 1000.0,
    "milligram": 0.001,
    "pound": 453.59237,
    "ounce": 28.349523125,
}

TEMPERATURE_UNITS = {
    "celsius": {
        "to_base": lambda c: c,
        "from_base": lambda c: c,
    },
    "fahrenheit": {
        "to_base": lambda f: (f - 32) * 5 / 9,
        "from_base": lambda c: (c * 9 / 5) + 32,
    },
    "kelvin": {
        "to_base": lambda k: k - 273.15,
        "from_base": lambda c: c + 273.15,
    },
}

CATEGORIES = {
    "length": LENGTH_UNITS,
    "weight": WEIGHT_UNITS,
}

UNIT_ALIASES = {
    "m": "meter", "meters": "meter",
    "km": "kilometer", "kilometers": "kilometer",
    "cm": "centimeter", "centimeters": "centimeter",
    "mm": "millimeter", "millimeters": "millimeter",
    "mi": "mile", "miles": "mile",
    "yd": "yard", "yards": "yard",
    "ft": "foot", "feet": "foot",
    "in": "inch", "inches": "inch",
    "g": "gram", "grams": "gram",
    "kg": "kilogram", "kilograms": "kilogram",
    "mg": "milligram", "milligrams": "milligram",
    "lbs": "pound", "lb": "pound", "pounds": "pound",
    "oz": "ounce", "ounces": "ounce",
    "c": "celsius", "f": "fahrenheit", "k": "kelvin",
}


def normalize_unit(unit_str: str) -> str:
    """Normalizes a unit string and resolves aliases."""
    clean_unit = unit_str.lower().strip()
    return UNIT_ALIASES.get(clean_unit, clean_unit)


def convert(value: float, from_unit: str, to_unit: str, category: str = None) -> float:
    """Master conversion entry point."""
    norm_from = normalize_unit(from_unit)
    norm_to = normalize_unit(to_unit)

    # Temperature branch
    if norm_from in TEMPERATURE_UNITS or norm_to in TEMPERATURE_UNITS:
        if norm_from not in TEMPERATURE_UNITS:
            raise UnknownUnitError(f"Unknown temperature unit: '{from_unit}'")
        if norm_to not in TEMPERATURE_UNITS:
            raise UnknownUnitError(f"Unknown temperature unit: '{to_unit}'")
        
        celsius_val = TEMPERATURE_UNITS[norm_from]["to_base"](value)
        return TEMPERATURE_UNITS[norm_to]["from_base"](celsius_val)

    # Category auto-detection
    if category is None:
        for cat_name, unit_dict in CATEGORIES.items():
            if norm_from in unit_dict and norm_to in unit_dict:
                category = cat_name
                break
        if category is None:
            raise IncompatibleUnitsError(
                f"Cannot convert from '{from_unit}' to '{to_unit}' (mismatched or unknown categories)."
            )

    if category not in CATEGORIES:
        raise UnknownCategoryError(f"Unknown category: '{category}'")

    unit_dict = CATEGORIES[category]

    if norm_from not in unit_dict:
        raise UnknownUnitError(f"Unknown unit '{from_unit}' in category '{category}'")
    if norm_to not in unit_dict:
        raise UnknownUnitError(f"Unknown unit '{to_unit}' in category '{category}'")

    base_value = value * unit_dict[norm_from]
    return base_value / unit_dict[norm_to]


if __name__ == "__main__":
    print("--- Stage 3 Alias & Routing Tests ---")
    
    # 5 km to mi (using shortcuts)
    res1 = convert(5, "km", "mi")
    print(f"5 km = {res1:.4f} mi")

    # 100 f to c (using temperature shortcuts)
    res2 = convert(100, "f", "c")
    print(f"100 F = {res2:.2f} C")

    # 10 lbs to kg
    res3 = convert(10, "lbs", "kg")
    print(f"10 lbs = {res3:.4f} kg")