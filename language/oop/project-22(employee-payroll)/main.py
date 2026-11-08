# from abc import ABC, abstractmethod


# class Employee(ABC):
#     def __init__(self, name, employee_id):
#         self.name = name
#         self.employee_id = employee_id

#     @abstractmethod
#     def calculate_salary(self):
#         pass


# class SalariedEmployee(Employee):
#     def __init__(self, name, employee_id, salary, work_days):
#         super().__init__(name, employee_id)
#         self.__monthly_salary = salary
#         self.__work_days = work_days

#     @property
#     def salary(self):
#         return self.__monthly_salary

#     @property
#     def work_days(self):
#         return self.__work_days

#     def calculate_salary(self):
#         return self.salary * self.work_days


# class HourlyEmployee(Employee):
#     hourly_rate_amount = 5

#     def __init__(self, name, employee_id, hourly_worked):
#         super().__init__(name, employee_id)
#         self.__hourly_worked = hourly_worked

#     @property
#     def hourly_worked(self):
#         return self.__hourly_worked

#     def calculate_salary(self):
#         return self.hourly_worked * self.hourly_rate_amount


# class CommissionEmployee(Employee):
#     commission_rate = 10

#     def __init__(self, name, employee_id, base_salary, sales_count):
#         super().__init__(name, employee_id)
#         self.__sales_count = sales_count
#         self.__base_salary = base_salary

#     @property
#     def base_salary(self):
#         return self.__base_salary

#     @property
#     def sales_count(self):
#         return self.__sales_count

#     def calculate_salary(self):
#         return self.base_salary + (
#             self.sales_count * self.commission_rate
#         )


# # -----------------------------
# # Test objects / class instances
# # -----------------------------

# employee1 = SalariedEmployee("John", 101, 3000, 22)
# employee2 = HourlyEmployee("Mary", 102, 160)
# employee3 = CommissionEmployee("David", 103, 2000, 50)


# # Test SalariedEmployee
# print("Salaried Employee")
# print("Name:", employee1.name)
# print("Employee ID:", employee1.employee_id)
# print("Salary:", employee1.calculate_salary())

# print("--------------------")

# # Test HourlyEmployee
# print("Hourly Employee")
# print("Name:", employee2.name)
# print("Employee ID:", employee2.employee_id)
# print("Hours Worked:", employee2.hourly_worked)
# print("Salary:", employee2.calculate_salary())

# print("--------------------")

# # Test CommissionEmployee
# print("Commission Employee")
# print("Name:", employee3.name)
# print("Employee ID:", employee3.employee_id)
# print("Base Salary:", employee3.base_salary)
# print("Sales Count:", employee3.sales_count)
# print("Salary:", employee3.calculate_salary())















from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation


# ==================== ABSTRACT EMPLOYEE ====================

class Employee(ABC):
    def __init__(self, name, employee_id):
        if not isinstance(name, str):
            raise TypeError("Employee name must be a string.")

        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if isinstance(employee_id, bool) or not isinstance(
            employee_id, (str, int)
        ):
            raise TypeError("Employee ID must be a string or integer.")

        if not str(employee_id).strip():
            raise ValueError("Employee ID cannot be empty.")

        self.__name = name.strip()
        self.__employee_id = str(employee_id).strip()

    @property
    def name(self):
        return self.__name

    @property
    def employee_id(self):
        return self.__employee_id

    @staticmethod
    def to_decimal(value):
        if isinstance(value, bool):
            raise TypeError("Compensation must be numeric.")

        if not isinstance(value, (int, float, Decimal)):
            raise TypeError("Compensation must be numeric.")

        try:
            amount = Decimal(str(value))
        except (InvalidOperation, ValueError):
            raise ValueError("Invalid compensation amount.")

        if not amount.is_finite():
            raise ValueError("Compensation must be finite.")

        return amount

    @classmethod
    def validate_nonnegative(cls, value, field_name):
        amount = cls.to_decimal(value)

        if amount < 0:
            raise ValueError(f"{field_name} cannot be negative.")

        return amount

    @classmethod
    def validate_positive(cls, value, field_name):
        amount = cls.to_decimal(value)

        if amount <= 0:
            raise ValueError(f"{field_name} must be greater than zero.")

        return amount

    @abstractmethod
    def calculate_salary(self):
        """Each employee type must calculate its own salary."""
        pass

    def display_details(self):
        return (
            f"Employee ID: {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"Employee Type: {type(self).__name__}\n"
            f"Salary: ₦{self.calculate_salary():,.2f}"
        )


# ==================== SALARIED EMPLOYEE ====================

class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)

        self.__monthly_salary = self.validate_positive(
            monthly_salary, "Monthly salary"
        )

    @property
    def monthly_salary(self):
        return self.__monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


# ==================== HOURLY EMPLOYEE ====================

class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)

        self.__hourly_rate = self.validate_positive(
            hourly_rate, "Hourly rate"
        )

        self.__hours_worked = self.validate_nonnegative(
            hours_worked, "Hours worked"
        )

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# ==================== COMMISSION EMPLOYEE ====================

class CommissionEmployee(Employee):
    def __init__(
        self,
        name,
        employee_id,
        base_salary,
        sales_amount,
        commission_rate
    ):
        super().__init__(name, employee_id)

        self.__base_salary = self.validate_nonnegative(
            base_salary, "Base salary"
        )

        self.__sales_amount = self.validate_nonnegative(
            sales_amount, "Sales amount"
        )

        self.__commission_rate = self.to_decimal(commission_rate)

        if not Decimal("0") <= self.__commission_rate <= Decimal("100"):
            raise ValueError(
                "Commission rate must be between 0 and 100 percent."
            )

    @property
    def base_salary(self):
        return self.__base_salary

    @property
    def sales_amount(self):
        return self.__sales_amount

    @property
    def commission_rate(self):
        return self.__commission_rate

    def calculate_salary(self):
        commission = (
            self.sales_amount * self.commission_rate / Decimal("100")
        )

        return self.base_salary + commission


# ==================== CONTRACT EMPLOYEE ====================
# Example of adding a new category without changing the payroll report.

class ContractEmployee(Employee):
    def __init__(self, name, employee_id, contract_payment):
        super().__init__(name, employee_id)

        self.__contract_payment = self.validate_positive(
            contract_payment, "Contract payment"
        )

    def calculate_salary(self):
        return self.__contract_payment


# ==================== PAYROLL REPORT ====================

def generate_payroll_report(employees):
    print("\n" + "=" * 65)
    print("PAYROLL REPORT")
    print("=" * 65)

    total_payroll = Decimal("0")

    for employee in employees:
        salary = employee.calculate_salary()
        total_payroll += salary

        print(
            f"ID: {employee.employee_id} | "
            f"Name: {employee.name} | "
            f"Type: {type(employee).__name__} | "
            f"Salary: ₦{salary:,.2f}"
        )

    print("-" * 65)
    print(f"Total payroll: ₦{total_payroll:,.2f}")
    print("=" * 65)

    return total_payroll


# ==================== CREATE EMPLOYEES ====================

employee1 = SalariedEmployee(
    "John", 101, 300000
)

employee2 = HourlyEmployee(
    "Mary", 102, 2500, 160
)

employee3 = CommissionEmployee(
    "David", 103, 100000, 500000, 10
)

employee4 = ContractEmployee(
    "Grace", 104, 180000
)


# ==================== POLYMORPHISM TEST ====================

employees = [
    employee1,
    employee2,
    employee3,
    employee4
]

generate_payroll_report(employees)


# ==================== ABSTRACT CLASS TEST ====================

print("\n--- ABSTRACT CLASS TEST ---")

try:
    employee = Employee("Alex", 105)
except TypeError as error:
    print("Cannot instantiate Employee:", error)


# ==================== INCOMPLETE SUBCLASS TEST ====================

class InternEmployee(Employee):
    pass


print("\n--- INCOMPLETE SUBCLASS TEST ---")

try:
    intern = InternEmployee("Sam", 106)
except TypeError as error:
    print("Cannot instantiate InternEmployee:", error)


# ==================== VALIDATION TESTS ====================

print("\n--- VALIDATION TESTS ---")

try:
    SalariedEmployee("Alex", 107, -50000)
except ValueError as error:
    print("Invalid salary:", error)

try:
    HourlyEmployee("Sam", 108, 2000, -10)
except ValueError as error:
    print("Invalid hours:", error)

try:
    CommissionEmployee("Taylor", 109, 50000, 100000, 150)
except ValueError as error:
    print("Invalid commission rate:", error)
