
# from uuid import uuid4
# from decimal import Decimal, InvalidOperation


# class Employee:
#     employees_record = []

#     def __init__(self, name: str, position: str):
#         if not isinstance(name, str) or not name.strip():
#             raise ValueError("Employee name cannot be empty.")

#         if not isinstance(position, str) or not position.strip():
#             raise ValueError("Employee position cannot be empty.")

#         self.name = name.strip()
#         self.position = position.strip()
#         self.__employee_id = f"employee-{uuid4().hex}"

#     @property
#     def employee_id(self) -> str:
#         return self.__employee_id

#     @property
#     def salary(self) -> Decimal:
#         raise NotImplementedError("Subclasses must define salary.")

#     def calculate_salary(self) -> Decimal:
#         return self.salary

#     @staticmethod
#     def _to_decimal(amount) -> Decimal:
#         if isinstance(amount, bool) or not isinstance(
#             amount, (int, float, Decimal)
#         ):
#             raise TypeError("Amount must be a number.")

#         try:
#             value = Decimal(str(amount))
#         except (InvalidOperation, ValueError):
#             raise ValueError("Amount must be a valid number.")

#         if not value.is_finite():
#             raise ValueError("Amount must be finite.")

#         return value

#     @classmethod
#     def _validate_amount(cls, amount) -> Decimal:
#         value = cls._to_decimal(amount)

#         if value <= 0:
#             raise ValueError("Amount must be greater than zero.")

#         return value

#     @classmethod
#     def register_employee(cls, employee):
#         if not isinstance(employee, Employee):
#             raise TypeError("Employee must be an Employee instance.")

#         record = {
#             "employee_id": employee.employee_id,
#             "employee_type": type(employee).__name__,
#             "employee_name": employee.name,
#             "employee_position": employee.position,
#             "employee_salary": str(employee.calculate_salary()),
#         }

#         cls.employees_record.append(record)
#         return employee.employee_id


# class FullTimeEmployee(Employee):
#     def __init__(self, name: str, position: str, monthly_salary):
#         super().__init__(name, position)
#         self.__salary = self._validate_amount(monthly_salary)

#     @property
#     def salary(self) -> Decimal:
#         return self.__salary


# class PartTimeEmployee(Employee):
#     def __init__(
#         self, name: str, position: str, hourly_rate, hours_worked
#     ):
#         super().__init__(name, position)
#         self.__hourly_rate = self._validate_amount(hourly_rate)
#         self.__hours_worked = self._validate_amount(hours_worked)

#     @property
#     def salary(self) -> Decimal:
#         return self.__hourly_rate * self.__hours_worked


# class ContractEmployee(Employee):
#     def __init__(
#         self, name: str, position: str, contract_payment_amount
#     ):
#         super().__init__(name, position)
#         self.__contract_payment_amount = self._validate_amount(
#             contract_payment_amount
#         )

#     @property
#     def salary(self) -> Decimal:
#         return self.__contract_payment_amount


# full_time = FullTimeEmployee(
#     "John Doe", "Software Engineer", 500000
# )

# part_time = PartTimeEmployee(
#     "Jane Smith", "Data Analyst", 2500, 80
# )

# contract = ContractEmployee(
#     "David James", "UI Designer", 150000
# )

# Employee.register_employee(full_time)
# Employee.register_employee(part_time)
# Employee.register_employee(contract)

# # Test salary calculations
# print("\n--- Salary Calculations ---")
# print(f"{full_time.name}: {full_time.calculate_salary()}")
# print(f"{part_time.name}: {part_time.calculate_salary()}")
# print(f"{contract.name}: {contract.calculate_salary()}")

# # Test employee IDs
# print("\n--- Employee IDs ---")
# print(full_time.employee_id)
# print(part_time.employee_id)
# print(contract.employee_id)

# # Test shared employee records
# print("\n--- All Employee Records ---")
# for employee in Employee.employees_record:
#     print(employee)
















from uuid import uuid4
from decimal import Decimal, InvalidOperation
from math import isfinite


class Employee:
    employees_record = {}

    def __init__(self, name: str, position: str):
        if not isinstance(name, str):
            raise TypeError("Employee name must be a string.")

        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if not isinstance(position, str):
            raise TypeError("Employee position must be a string.")

        if not position.strip():
            raise ValueError("Employee position cannot be empty.")

        self.__name = name.strip()
        self.__position = position.strip()
        self.__employee_id = f"EMP-{uuid4().hex[:12].upper()}"

    @property
    def employee_id(self) -> str:
        return self.__employee_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def position(self) -> str:
        return self.__position

    @property
    def salary(self) -> Decimal:
        raise NotImplementedError(
            "Subclasses must define their salary calculation."
        )

    def calculate_salary(self) -> Decimal:
        return self.salary

    def display_details(self) -> str:
        return (
            f"Employee ID: {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"Position: {self.position}\n"
            f"Employee type: {type(self).__name__}\n"
            f"Pay: ₦{self.calculate_salary():,.2f}"
        )

    @staticmethod
    def _to_decimal(amount) -> Decimal:
        if isinstance(amount, bool) or not isinstance(
            amount, (int, float, Decimal)
        ):
            raise TypeError("Amount must be numeric.")

        if isinstance(amount, float) and not isfinite(amount):
            raise ValueError("Amount must be finite.")

        try:
            value = Decimal(str(amount))
        except (InvalidOperation, ValueError):
            raise ValueError("Amount must be a valid number.")

        if not value.is_finite():
            raise ValueError("Amount must be finite.")

        return value

    @classmethod
    def _validate_positive_amount(cls, amount) -> Decimal:
        value = cls._to_decimal(amount)

        if value <= 0:
            raise ValueError("Amount must be greater than zero.")

        return value

    @classmethod
    def _validate_nonnegative_amount(cls, amount) -> Decimal:
        value = cls._to_decimal(amount)

        if value < 0:
            raise ValueError("Amount cannot be negative.")

        return value

    @classmethod
    def register_employee(cls, employee):
        if not isinstance(employee, Employee):
            raise TypeError("Expected an Employee instance.")

        employee_id = employee.employee_id

        if employee_id in Employee.employees_record:
            raise ValueError("Employee is already registered.")

        Employee.employees_record[employee_id] = {
            "employee_id": employee_id,
            "employee_type": type(employee).__name__,
            "employee_name": employee.name,
            "employee_position": employee.position,
        }

        return employee_id

    @classmethod
    def get_employee_records(cls):
        return [
            record.copy()
            for record in Employee.employees_record.values()
        ]


class FullTimeEmployee(Employee):
    def __init__(self, name: str, position: str, monthly_salary):
        super().__init__(name, position)
        self.__monthly_salary = self._validate_positive_amount(
            monthly_salary
        )

    @property
    def salary(self) -> Decimal:
        return self.__monthly_salary


class PartTimeEmployee(Employee):
    def __init__(
        self,
        name: str,
        position: str,
        hourly_rate,
        hours_worked
    ):
        super().__init__(name, position)

        self.__hourly_rate = self._validate_positive_amount(hourly_rate)
        self.__hours_worked = self._validate_nonnegative_amount(
            hours_worked
        )

    @property
    def hourly_rate(self) -> Decimal:
        return self.__hourly_rate

    @property
    def hours_worked(self) -> Decimal:
        return self.__hours_worked

    @property
    def salary(self) -> Decimal:
        return self.__hourly_rate * self.__hours_worked


class ContractEmployee(Employee):
    def __init__(
        self,
        name: str,
        position: str,
        contract_payment_amount
    ):
        super().__init__(name, position)

        self.__contract_payment_amount = (
            self._validate_positive_amount(contract_payment_amount)
        )

    @property
    def salary(self) -> Decimal:
        return self.__contract_payment_amount


# ==================== TESTING ====================

full_time = FullTimeEmployee(
    "John Doe", "Software Engineer", 500000
)

part_time = PartTimeEmployee(
    "Jane Smith", "Data Analyst", 2500, 80
)

contract = ContractEmployee(
    "David James", "UI Designer", 150000
)

# A part-time employee who has not worked any hours yet.
new_part_time = PartTimeEmployee(
    "Grace Williams", "Support Assistant", 1800, 0
)

# Register employees.
for employee in [full_time, part_time, contract, new_part_time]:
    Employee.register_employee(employee)

# 1. Polymorphism: process all employee types with the same method.
print("\n--- EMPLOYEE PAYROLL ---")

employees = [full_time, part_time, contract, new_part_time]

for employee in employees:
    print(
        f"{employee.name} | "
        f"{type(employee).__name__} | "
        f"Pay: ₦{employee.calculate_salary():,.2f}"
    )

# 2. Display employee details.
print("\n--- EMPLOYEE DETAILS ---")

for employee in employees:
    print(employee.display_details())
    print("-" * 40)

# 3. Display the shared employee registry.
print("\n--- REGISTERED EMPLOYEES ---")

for record in Employee.get_employee_records():
    print(record)

# 4. Check duplicate registration protection.
print("\n--- DUPLICATE REGISTRATION TEST ---")

try:
    Employee.register_employee(full_time)
except ValueError as error:
    print("Registration rejected:", error)

# 5. Test invalid salary and hours.
print("\n--- VALIDATION TESTS ---")

try:
    FullTimeEmployee("Alex", "Developer", -50000)
except ValueError as error:
    print("Invalid salary:", error)

try:
    PartTimeEmployee("Sam", "Assistant", 2000, -5)
except ValueError as error:
    print("Invalid hours:", error)

try:
    PartTimeEmployee("Taylor", "Assistant", 2000, True)
except TypeError as error:
    print("Invalid Boolean hours:", error)

try:
    ContractEmployee("Morgan", "Designer", float("inf"))
except ValueError as error:
    print("Invalid contract payment:", error)
