# Python Object-Oriented Programming (OOP) Practice Problems

## Level 1 — Beginner: Class and Object Fundamentals

_Problems 1–6 · Build confidence with class design and object state._

### 1\. Student Profile Manager

**Beginner**

Create a `Student` class that stores a student's name, age, and course.

**Requirements**

- Create at least three student objects with different information.
- Add a method that displays a student's details.
- Add a method that determines whether the student is an adult.
- Demonstrate that updating one student's information does not accidentally change another student's information.

### 2\. Bank Account

Create a `BankAccount` class with an account holder, account number, and balance.

**Requirements**

- Implement deposit and withdrawal methods.
- Reject negative deposits and withdrawals.
- Prevent withdrawals that exceed the available balance.
- Add a method to display the current balance.
- Test multiple transactions on the same account.

### 3\. Product Inventory

Build a `Product` class with a name, price, and stock quantity.



**Requirements**

- Add stock and remove stock.
- Prevent the stock quantity from becoming negative.
- Calculate the total inventory value for an individual product.
- Create several products and calculate the total value of all inventory.

### 4\. Rectangle Calculator

Build a `Rectangle` class that stores width and height.

**Requirements**

- Calculate area and perimeter.
- Determine whether the rectangle is a square.
- Reject zero or negative dimensions.
- Create multiple rectangles and compare their areas.

### 5\. Employee Payroll

Create an `Employee` class containing a name, hourly rate, and hours worked.

**Requirements**

- Calculate gross pay.
- Calculate overtime pay using a rule you define and document.
- Reject invalid hourly rates and hours worked.
- Create multiple employees and generate a payroll summary.

### 6\. Class Attributes vs Instance Attributes

Build a `LibraryBook` class that tracks book titles, authors, and a shared library name.

**Requirements**

- Store book-specific details on individual objects.
- Store a shared library property at the class level.
- Change the shared library name and investigate how instances respond.
- Add a class-level counter for the number of books registered.
- Demonstrate the difference between changing a class attribute and creating an instance attribute with the same name.

**Level 1 completion test:** You should be able to create classes from requirements, manage object state, and distinguish instance attributes from class attributes without relying on memorized templates.

---

## Level 2 — Beginner to Intermediate: Encapsulation and Properties

_Problems 7–12 · Protect data and control how objects change._

### 7\. Validated Bank Account

Upgrade the bank account from Problem 2.

**Requirements**

- Control how the balance can be changed.
- Make deposits and withdrawals the supported ways to change the balance.
- Prevent direct changes from bypassing your account rules.
- Ensure every transaction preserves the account's valid state.
- Test attempts to bypass your safeguards.

### 8\. Temperature Converter with Properties

Create a `Temperature` class that stores a temperature in Celsius.

**Requirements**

- Expose a Celsius property.
- Provide a Fahrenheit property that converts the value.
- Validate values when the Celsius property is assigned.
- Ensure changing Celsius automatically affects the Fahrenheit reading.
- Avoid storing two independent values that can become inconsistent.

### 9\. User Account Settings

Build a `UserAccount` class with a username, email address, and password.

**Requirements**

- Validate usernames and email addresses according to rules you define.
- Control changes to the email address through a property setter.
- Prevent the password from being exposed through ordinary account-display output.
- Implement an account deactivation operation.
- Decide what deleting an optional profile property should mean and implement the behavior.

### 10\. Shopping Cart

Create `Product` and `ShoppingCart` classes.

**Requirements**

- Add products with quantities.
- Remove products and update quantities.
- Calculate subtotals and the cart total.
- Prevent invalid quantities.
- Ensure the cart's total is calculated from its current contents rather than becoming stale after changes.

### 11\. Property Getter, Setter, and Deleter

Create a `Profile` class with an optional biography.

**Requirements**

- Use a property getter to retrieve the biography.
- Use a setter to validate updates.
- Use a deleter to clear the biography.
- Define what happens when the biography is empty or deleted.
- Test all three operations, including invalid assignments.

### 12\. Secure Digital Wallet

Build a `DigitalWallet` class.

**Requirements**

- Support deposits, payments, refunds, and balance checks.
- Reject invalid transactions.
- Record a transaction history.
- Keep the balance consistent with successful transactions.
- Make it impossible for an invalid operation to silently change the balance.

**Level 2 completion test:** You should understand that encapsulation is about controlling and maintaining valid object state, not merely adding underscores to attribute names. Python properties provide a standard mechanism for managing attribute access.

Python 3.14.8 documentation\
+1

---

## Level 3 — Intermediate: Inheritance and `super()`

_Problems 13–18 · Reuse behavior while allowing specialized classes._

### 13\. Employee Types

Create a parent `Employee` class and subclasses for `FullTimeEmployee`, `PartTimeEmployee`, and `ContractEmployee`.

**Requirements**

- Share common employee information and behavior in the parent class.
- Implement different salary calculations for each subclass.
- Override a common method where necessary.
- Process a collection of employees and calculate their individual pay.

### 14\. Multilevel Inheritance: School System

Design a three-level hierarchy: `Person`, `Student`, and `GraduateStudent`.

**Requirements**

- Each level must introduce its own relevant attributes or behaviors.
- A graduate student must retain the features of both parent levels.
- Demonstrate which methods and attributes are inherited.
- Override at least one inherited method.
- Verify the relationships using `isinstance()` and `issubclass()`.

### 15\. `super()` and Constructor Chaining

Build a hierarchy for `Vehicle`, `Car`, and `ElectricCar`.

**Requirements**

- Each class must add its own initialization data.
- Use `super()` to initialize inherited state.
- Extend a parent method without unnecessarily duplicating its entire implementation.
- Ensure every required attribute is initialized correctly.
- Test creating instances at each level.

### 16\. Payment Method Hierarchy

Create a `PaymentMethod` parent class with `CreditCardPayment`, `BankTransferPayment`, and `MobileWalletPayment` subclasses.

**Requirements**

- Give the subclasses a shared payment interface.
- Implement their payment behavior differently.
- Validate payment amounts.
- Produce a transaction result for each payment method.
- Demonstrate that a new payment type can be added without rewriting the main checkout workflow.

### 17\. Multilevel Inheritance: Online Store Users

Design a hierarchy containing `User`, `Customer`, `PremiumCustomer`, and `BusinessCustomer`.

**Requirements**

- Introduce different capabilities at each level.
- Override discount or benefits calculations where appropriate.
- Use `super()` correctly when extending inherited behavior.
- Ensure a subclass does not accidentally break the rules of its parent.
- Explain in your own notes which behaviors genuinely belong in the parent class.

### 18\. Inheritance Design Review

Imagine you have a `Bird` parent class with a `fly()` method, and you want to create subclasses for eagles, penguins, and ostriches.

**Requirements**

- Design a hierarchy that doesn't require every bird to fly.
- Preserve shared bird behaviors.
- Support different capabilities without forcing unrelated subclasses to implement unsuitable behavior.
- Demonstrate the design with at least three bird types.

**Level 3 completion test:** You should know how inheritance, method overriding, multilevel hierarchies, and `super()` work. You should also recognize when inheritance creates a poor design. Python's class documentation explains inheritance, overriding, and the method lookup mechanism.

Python 3.14.8 documentation\
+1

---

## Level 4 — Intermediate to Advanced: Polymorphism and Abstraction

_Problems 19–24 · Work with different objects through consistent interfaces._

### 19\. Shape Area Calculator — Polymorphism

Create `Circle`, `Rectangle`, and `Triangle` classes.

**Requirements**    

- Give each class a common area-calculation method.
- Implement the calculation according to each shape's geometry.
- Write one function that accepts different shape objects and calculates their areas.
- Do not write a separate conditional branch for every concrete shape in that function.

### 20\. Duck Typing: Notification System

Create separate objects for email, SMS, and push notifications.

**Requirements**

- Give each object a compatible notification method.
- Build one function that sends a notification using that method.
- Allow the function to work with a new notification class without changing its internal logic.
- Test a compatible object that doesn't inherit from any notification base class.
- Test what happens when an object lacks the required behavior.

### 21\. Abstract Payment Processor

Create an abstract `PaymentProcessor` class.

**Requirements**

- Define the required payment operation as an abstract method.
- Implement at least three concrete payment processors.
- Prevent instantiation of the incomplete abstract class.
- Process a list of concrete processors through a common interface.
- Test a subclass that fails to implement the required abstract behavior.

### 22\. Abstract Employee Payroll

Design an abstract `Employee` class with subclasses for salaried, hourly, and commission-based employees.

**Requirements**

- Define a common abstract salary-calculation contract.
- Implement a different formula for each employee type.
- Store and validate relevant compensation data.
- Generate a payroll report without depending on each subclass's concrete type.
- Ensure the design can accommodate another employee category.

### 23\. Duck-Typed Report Exporter

Build a reporting function that can export data through different objects, such as CSV, JSON, or plain-text exporters.

**Requirements**

- Give each exporter a common export behavior without requiring a shared parent class.
- Let the reporting function work with any compatible exporter.
- Add a new exporter without modifying the reporting function.
- Handle invalid exporters in a deliberate and understandable way.

### 24\. Abstract File Storage System

Create an abstract `Storage` class with concrete implementations such as `LocalStorage` and `MemoryStorage`.

**Requirements**

- Define common operations for saving and retrieving data.
- Implement each storage type differently.
- Write an application component that depends on the common storage interface.
- Switch storage implementations without rewriting that component.
- Test missing records and invalid storage operations.

**Level 4 completion test:** You should be able to distinguish inheritance-based polymorphism from duck typing, design abstract base classes, and write code that depends on behavior rather than a specific concrete class. Python's `abc` module supports abstract methods and prevents instantiation when required methods remain unimplemented.

Python 3.12.15 documentation\
+1

---

## Level 5 — Advanced: Object Relationships and Special Methods

_Problems 25–30 · Combine multiple concepts into maintainable applications._

### 25\. Composition: Restaurant Ordering System

Build a restaurant ordering system using separate `MenuItem`, `OrderItem`, `Order`, and `Customer` classes.

**Requirements**

- An order contains multiple order items.
- Each order item refers to a menu item and quantity.
- Calculate item totals, order totals, and applicable discounts.
- Add and remove items while keeping totals correct.
- Demonstrate how the objects collaborate without placing the entire application inside one class.

### 26\. Aggregation: School Management System

Build `Student`, `Teacher`, `Course`, and `School` classes.

**Requirements**

- A school manages collections of students, teachers, and courses.
- Courses can have enrolled students and assigned teachers.
- Objects should be able to exist independently of the school object.
- Support enrollment, withdrawal, and teacher reassignment.
- Prevent duplicate enrollment and invalid assignments.
- Explain how your design demonstrates aggregation rather than ownership through composition.

### 27\. Class and Static Methods: Object Factory

Build a `Product` class that supports normal construction and alternative ways to create products.

**Requirements**

- Use a class method to create a product from a dictionary.
- Use another class method to create a product from a formatted string.
- Use a static method for a validation or calculation that doesn't need instance or class state.
- Ensure the alternative constructors still work correctly when the class is subclassed.
- Demonstrate when an ordinary instance method would be the better choice.

### 28\. Dunder Methods: Custom Money Class

Create a `Money` class representing monetary amounts and currencies.

**Requirements**

- Implement readable string and developer representations using `__str__` and `__repr__`.
- Support addition and subtraction between compatible amounts.
- Support comparisons between compatible amounts.
- Define what should happen when currencies differ.
- Implement equality consistently.
- Test the behavior of your objects with Python operators.

### 29\. Nested Classes: Computer Configuration

Design a `Computer` class containing a nested class that represents a configuration or component specification.

**Requirements**

- The nested class should represent a meaningful concept associated with the outer class.
- Create and use instances of the nested class.
- Keep the computer's operations separate from the configuration's responsibilities.
- Demonstrate how the nested class is accessed.
- Decide whether nesting actually improves this design and explain why.

### 30\. Final Project: E-Commerce Management System

Build a small e-commerce application that combines the major OOP concepts into one working system.

**Required components**

- `User`, `Customer`, and `Admin` classes.
- `Product`, `ShoppingCart`, `CartItem`, and `Order` classes.
- An abstract payment interface and at least two concrete payment implementations.
- A notification interface implemented by multiple notification types, including one based on duck typing.
- Properties for validating important attributes.
- Class or static methods where they provide genuine value.
- Useful dunder methods for selected domain objects.

**Required behavior**

- Register customers and manage products.
- Add and remove products from carts.
- Validate stock before checkout.
- Calculate totals and apply discounts.
- Process payments and update order status.
- Notify customers of order results.
- Maintain an order history.
- Reject invalid operations without leaving the system in an inconsistent state.

**Final test:** You should be able to add a new payment method or notification type without rewriting the core checkout workflow. Explain which concepts you used, why you used them, and what you would improve if the application grew larger.