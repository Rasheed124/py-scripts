

# class Employee:
#     _product_list = {}

#     def __init__(self, name: str, hourly_rate : int | float, hours_worked: int):
#         if not name:
#             raise ValueError("Name cannot be empty.")
        
#         if not isinstance(hourly_rate, (int, float)) or isinstance(hourly_rate, bool):
#             raise TypeError("Add a numeric valid hourly rate.")

#         if not isinstance(hours_worked, int) or isinstance(hours_worked, bool):
#             raise TypeError("Hours worked must be an integer.")

#         if hourly_rate <= 0:
#             raise ValueError("Hourly rate must be greater than zero.")

#         if hours_worked <= 0:
#             raise ValueError("Hours worked cannot be negative and must be greater than zero .")

#         self.name = name
#         self.__hourly_rate = hourly_rate
#         self.__hours_worked = hours_worked


#     @property
#     def hourly_rate(self):
#         return self.__hourly_rate
    
#     @property
#     def hours_worked(self):
#         return self.__hours_worked



#     def calculate_gross_pay(self):
#         return self.hourly_rate * self.hours_worked

    
#     def calculate_overtime_pay(self):
#         calc_gross_pay = 0
#         if self.hours_worked  > 40:
#             calc_gross_pay =  self.hourly_rate * 1.5
#             return calc_gross_pay
#         else:
#             print("Employee not qualified for overtime pay")

    
#     def calculate_total_pay(self):
#         return self.calculate_gross_pay() + self.calculate_overtime_pay()
    
#     def display_pay_slip(self):
#         print(self.name)
#         # 
    

#     @property
#     def gross_pay(self):
#         return self.calculate_gross_pay()







# Ai reviw


class Employee:

    def __init__(self, name: str, hourly_rate: int | float,
                 hours_worked: int | float):

        if not isinstance(name, str):
            raise TypeError("Employee name must be a string.")

        if not name.strip():
            raise ValueError("Employee name cannot be empty.")

        if not isinstance(hourly_rate, (int, float)) or isinstance(hourly_rate, bool):
            raise TypeError("Hourly rate must be numeric.")

        if not isinstance(hours_worked, (int, float)) or isinstance(hours_worked, bool):
            raise TypeError("Hours worked must be numeric.")

        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be greater than zero.")

        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")

        self.name = name.strip()
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    @property
    def hourly_rate(self):
        return self.__hourly_rate

    @property
    def hours_worked(self):
        return self.__hours_worked

    @property
    def overtime_hours(self):
        return max(0, self.hours_worked - 40)

    @property
    def regular_hours(self):
        return min(self.hours_worked, 40)

    def calculate_gross_pay(self):
        return self.regular_hours * self.hourly_rate

    def calculate_overtime_pay(self):
        return self.overtime_hours * self.hourly_rate * 1.5

    def calculate_total_pay(self):
        return self.calculate_gross_pay() + self.calculate_overtime_pay()

    def display_pay_slip(self):
        return (
            "\n========== EMPLOYEE PAYSLIP ==========\n"
            f"Employee name: {self.name}\n"
            f"Hours worked: {self.hours_worked}\n"
            f"Hourly rate: ₦{self.hourly_rate:,.2f}\n"
            f"Regular hours: {self.regular_hours}\n"
            f"Regular pay: ₦{self.calculate_gross_pay():,.2f}\n"
            f"Overtime hours: {self.overtime_hours}\n"
            f"Overtime pay: ₦{self.calculate_overtime_pay():,.2f}\n"
            f"Total pay: ₦{self.calculate_total_pay():,.2f}\n"
            "======================================"
        )

    def __str__(self):
        return f"Employee(name={self.name!r})"


# Create three employees
employee1 = Employee("Rasheed", 2000, 35)
employee2 = Employee("Adeola", 2000, 40)
employee3 = Employee("Fatima", 2000, 45)

# Display payslips
print(employee1.display_pay_slip())
print(employee2.display_pay_slip())
print(employee3.display_pay_slip())

# Test individual calculations
print("\n--- Pay Calculation Tests ---")
print("Employee 1 gross pay:", employee1.calculate_gross_pay())
print("Employee 1 overtime pay:", employee1.calculate_overtime_pay())
print("Employee 1 total pay:", employee1.calculate_total_pay())

print("Employee 3 overtime hours:", employee3.overtime_hours)
print("Employee 3 overtime pay:", employee3.calculate_overtime_pay())
print("Employee 3 total pay:", employee3.calculate_total_pay())

# Test independent employee objects
print("\n--- Independent Employee Tests ---")
print(employee1.name, employee1.hours_worked)
print(employee2.name, employee2.hours_worked)
print(employee3.name, employee3.hours_worked)

# Test invalid inputs
print("\n--- Validation Tests ---")

invalid_employees = [
    ("Empty name", "", 2000, 40),
    ("Whitespace name", "   ", 2000, 40),
    ("Negative hourly rate", "John", -2000, 40),
    ("Negative hours", "John", 2000, -5),
    ("Boolean hourly rate", "John", True, 40),
    ("Boolean hours", "John", 2000, False),
    ("Non-string name", 123, 2000, 40),
]

for description, name, rate, hours in invalid_employees:
    try:
        Employee(name, rate, hours)
    except (TypeError, ValueError) as error:
        print(f"{description}: {type(error).__name__}: {error}")
