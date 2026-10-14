# class TemperatureConverter:

#     def __init__(self, celsius=None, fahrenheit=None):
#         if (celsius is None) == (fahrenheit is None):
#             raise ValueError(
#                 "Provide either celsius or fahrenheit, not both."
#             )

#         self.__celsius = None
#         self.__fahrenheit = None

#         if celsius is not None:
#             self.celsius = celsius
#         else:
#             self.fahrenheit = fahrenheit

#     def _validate_fahrenheit(self, fahrenheit):
#         if not isinstance(fahrenheit, (int, float)) or isinstance(fahrenheit, bool):
#             raise TypeError("fahrenheit must be numeric.")

#         if fahrenheit < -459.67:
#             raise ValueError(
#                 "Temperature cannot be below -459.67°F."
#             )
#         return fahrenheit

#     def _validate_celsius(self, celsius):
#         if not isinstance(celsius, (int, float)) or isinstance(celsius, bool):
#             raise TypeError("celsius must be numeric.")

#         if celsius < -273.15:
#             raise ValueError(
#                 "Temperature cannot be below -273.15°C."
#             )
#         return celsius

#     @property
#     def celsius(self) -> float:
#         if self.__celsius is None and self.__fahrenheit is not None:
#             return f"{((self.__fahrenheit - 32) * 5 / 9):.2f}"
#         return f"{self.__celsius:.2f}"

#     @property
#     def fahrenheit(self) -> float:
#         if self.__fahrenheit is None and self.__celsius is not None:
#             return f"{((self.__celsius * 9 / 5) + 32):.2f}"
#         return f"{self.__fahrenheit:.2f}"

#     @celsius.setter
#     def celsius(self, value: float) -> None:
#         self.__celsius = self._validate_celsius(value)
#         self.__fahrenheit = None

#     @fahrenheit.setter
#     def fahrenheit(self, value: float) -> None:
#         self.__fahrenheit = self._validate_fahrenheit(value)
#         self.__celsius = None

#     def convert(self, celsius=None, fahrenheit=None):
#         if (celsius is None) == (fahrenheit is None):
#             raise ValueError(
#                 "Provide either celsius or fahrenheit, not both."
#             )

#         if celsius is not None:
#             self.celsius = celsius
#             print(
#                 f"You converted Celsius to Fahrenheit: "
#                 f"{self.fahrenheit}"
#             )
#         else:
#             self.fahrenheit = fahrenheit
#             print(
#                 f"You converted Fahrenheit to Celsius: "
#                 f"{self.celsius}"
#             )

#         return self

#     def __str__(self):
#         if self.__celsius is not None:
#             direction = "Celsius to Fahrenheit"
#         else:
#             direction = "Fahrenheit to Celsius"

#         return f"You want to convert from {direction}"


# temp1 = TemperatureConverter(fahrenheit=25)
# print(temp1)
# print("Celsius:", temp1.celsius)
# print("Fahrenheit:", temp1.fahrenheit)

# temp2 = TemperatureConverter(celsius=25)
# print(temp2)
# print("Celsius:", temp2.celsius)
# print("Fahrenheit:", temp2.fahrenheit)

# temp1.convert(celsius=0)
# print("Updated Celsius:", temp1.celsius)
# print("Updated Fahrenheit:", temp1.fahrenheit)













class Temperature:

    def __init__(self, celsius: int | float):
        self.celsius = celsius

    def _validate_celsius(self, value: int | float) -> int | float:
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("Celsius must be a numeric value.")

        if value < -273.15:
            raise ValueError("Temperature cannot be below -273.15°C.")

        return value

    @property
    def celsius(self) -> int | float:
        return self.__celsius

    @celsius.setter
    def celsius(self, value: int | float) -> None:
        self.__celsius = self._validate_celsius(value)

    @property
    def fahrenheit(self) -> float:
        return (self.__celsius * 9 / 5) + 32

    def __str__(self) -> str:
        return (
            f"Temperature: {self.celsius:.2f}°C "
            f"({self.fahrenheit:.2f}°F)"
        )


# ==========================================
# 1. Create temperature objects
# ==========================================

temp1 = Temperature(25)
temp2 = Temperature(-10)
temp3 = Temperature(0)

print("--- Initial Temperatures ---")
print(temp1)  # 25°C = 77°F
print(temp2)  # -10°C = 14°F
print(temp3)  # 0°C = 32°F


# ==========================================
# 2. Change Celsius and observe Fahrenheit
# ==========================================

print("\n--- Update Celsius ---")

temp1.celsius = 30

print("Celsius:", temp1.celsius)
print("Fahrenheit:", temp1.fahrenheit)  # 86°F


# ==========================================
# 3. Test the absolute-zero boundary
# ==========================================

print("\n--- Absolute Zero ---")

temp3.celsius = -273.15

print("Celsius:", temp3.celsius)
print("Fahrenheit:", temp3.fahrenheit)  # Approximately -459.67°F


# ==========================================
# 4. Test invalid assignments
# ==========================================

print("\n--- Validation Tests ---")

invalid_values = [
    ("String", "hot"),
    ("Boolean", True),
    ("Below absolute zero", -300),
    ("None", None),
]

for description, value in invalid_values:
    previous_celsius = temp1.celsius

    try:
        temp1.celsius = value
    except (TypeError, ValueError) as error:
        print(f"{description}: {type(error).__name__}: {error}")

    print("Previous value preserved:", temp1.celsius == previous_celsius)


# ==========================================
# 5. Test independent objects
# ==========================================

print("\n--- Independent Objects ---")

temp1.celsius = 20

print("Temperature 1:", temp1)
print("Temperature 2:", temp2)
print("Temperature 3:", temp3)


# ==========================================
# 6. Confirm Fahrenheit is read-only
# ==========================================

print("\n--- Fahrenheit Property ---")

try:
    temp1.fahrenheit = 100
except AttributeError as error:
    print("Fahrenheit assignment rejected:", error)
