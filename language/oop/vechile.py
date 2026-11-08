class Vehicle:
    def __init__(self, make: str, model: str, year: str):
        self.__make = self._to_str(make)
        self.__model = self._to_str(model)
        self.__year = self._to_str(year)

    @property
    def make(self) -> str:
        return self.__make

    @property
    def model(self) -> str:
        return self.__model

    @property
    def year(self) -> str:
        return self.__year

    def display_vehicle_details(self) -> str:
        return (
            f"Vehicle Make: {self.make}\n"
            f"Vehicle Model: {self.model}\n"
            f"Vehicle Year: {self.year}\n"
        )

    @staticmethod
    def _to_str(value: str) -> str:
        if not isinstance(value, str):
            raise TypeError("Value must be a string.")

        if not value.strip():
            raise ValueError("Value cannot be empty.")

        return value.strip()


class Car(Vehicle):
    def __init__(
        self,
        make: str,
        model: str,
        year: str,
        no_of_doors: int,
        transmission_type: str,
    ):
        super().__init__(make, model, year)

        self.__no_of_doors = self._to_int(no_of_doors)
        self.__transmission_type = self._to_str(transmission_type)

    @property
    def no_of_doors(self) -> int:
        return self.__no_of_doors

    @property
    def transmission_type(self) -> str:
        return self.__transmission_type

    @staticmethod
    def _to_int(value: int) -> int:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("Number of doors must be an integer.")

        if value <= 0:
            raise ValueError("Number of doors must be greater than zero.")

        return value

    def display_vehicle_details(self) -> str:
        details = super().display_vehicle_details()

        return (
            details
            + f"Car Number of Doors: {self.no_of_doors}\n"
            + f"Car Transmission Type: {self.transmission_type}\n"
        )


class ElectricCar(Car):
    def __init__(
        self,
        make: str,
        model: str,
        year: str,
        no_of_doors: int,
        transmission_type: str,
        battery_capacity: str,
        estimated_driving_range: str,
    ):
        super().__init__(
            make,
            model,
            year,
            no_of_doors,
            transmission_type,
        )

        self.__battery_capacity = self._to_str(battery_capacity)
        self.__estimated_driving_range = self._to_str(
            estimated_driving_range
        )

    @property
    def electric_car_battery_capacity(self) -> str:
        return self.__battery_capacity

    @property
    def electric_car_estimated_driving_range(self) -> str:
        return self.__estimated_driving_range

    def display_vehicle_details(self) -> str:
        details = super().display_vehicle_details()

        return (
            details
            + f"Electric Car Battery Capacity: "
            f"{self.electric_car_battery_capacity}\n"
            + f"Electric Car Estimated Driving Range: "
            f"{self.electric_car_estimated_driving_range}\n"
        )


# Create objects
vehicle = Vehicle("Toyota", "Corolla", "2022")

car = Car(
    "Honda",
    "Accord",
    "2023",
    4,
    "Automatic",
)

electric_car = ElectricCar(
    "Tesla",
    "Model 3",
    "2025",
    4,
    "Automatic",
    "75 kWh",
    "500 km",
)


# Display details
print("--- Vehicle Details ---")
print(vehicle.display_vehicle_details())

print("--- Car Details ---")
print(car.display_vehicle_details())

print("--- Electric Car Details ---")
print(electric_car.display_vehicle_details())