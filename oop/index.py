# from car import Car

# car1 =  Car("Mustang", 2026, 'blue', True)
# car2 =  Car("Benz", 2026, 'blue', False)

# print(car1)
# print(car2)


# print(Car.num_cars)



# ================================= Inheritance ==============


########################## Normal Inheritance


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f"{self.name} is eating"

#     def __str__(self):
#         return f"{self.name} is an animal"



# class Goat(Animal):
#     pass
# class Cat(Animal):
#     pass


# cat  =  Cat("mew")
# goat  =  Goat("eran")






######################## MultiLevel Inheritance



# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         return f"{self.name} is eating"

#     def __str__(self):
#         return f"{self.name} is an animal"



# class Prey(Animal):
#     pass
# class Predator(Animal):
#     def sleep(self):
#         return f"{self.name} is sleeping"


# class Rabbit(Animal):
#     pass

# class Fish(Prey, Predator):
#     pass


# fish  =  Fish("Tony")

# print(fish.eat())
# print(fish.sleep())





######################## Abstract Classes


# All methods call must be included in the children class
# They can't be instantiated

# abc - abstract base class

# from abc import ABC, abstractmethod


# class Vechicle(ABC):

#     @abstractmethod
#     def go(self):
#         pass


#     @abstractmethod
#     def stop(self):
#         pass



# class Car(Vechicle):
#     def go(self):
#         print("it can drive ")

#     def stop(self):
#         print("it can stop")


# car =  Car()



######################## Super With Inheritance method


# class Shape:
#     def __init__(self, color, is_filled):
#         self.color = color
#         self.is_filled = is_filled


#     def describe(self):
#         print(f"It is {self.color} and {'is filled' if self.is_filled else  'is not filled'}")


# class Rectangle(Shape):

#     def __init__(self, color, is_filled, side):
#         super().__init__(color, is_filled)
#         self.side = side

#     def describe(self):
#         print(f"The area is {self.side * 2} cm2 ")
#         return super().describe()


# class Triangle(Shape):
#     def __init__(self, color, is_filled, width, height):
#         super().__init__(color, is_filled)
#         self.width = width
#         self.height = height


# class Circle(Shape):
#     def __init__(self, color, is_filled, radius):
#         super().__init__(color, is_filled)
#         self.radius = radius



# circle =  Circle(color="Blue", is_filled=True, radius=20)
# rectangle =  Rectangle(color="White", is_filled=False, side=20)

# rectangle.describe()




######################## Polymorphism 


# --------------------------Inheritance way of Polymorphism

# from abc import ABC, abstractmethod


# class Shape:

#     @abstractmethod
#     def area(self):
#         pass
 
# class Rectangle(Shape):

#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return f" Area of is {self.side * 2} cm"


# class Triangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return f" Area is {self.width * self.height} cm"


# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return f" Area is { 3.142 * self.radius**2 } cm"


# class Pizza(Circle):
#     def __init__(self, toppin, pizzaRadius):
#         self.toppin =  toppin
#         super().__init__(radius=pizzaRadius)

# shapes = [Rectangle(3), Triangle(4, 5), Circle(6), Pizza('Pizza', 3)]

# for shape in shapes:
#     print(shape.area()) 




# --------------------------Duck typing way of Polymorphism

# class Animal:

#     alive = True

# class Cat(Animal):
#     def speak(self):
#         print("Meww")
# class Goat(Animal):
#     def speak(self):
#         print("Mehhhhh")

# class Car:
#     def speak(self):
#         print("Horning")

# animals  = [ Cat(), Goat(), Car()]

# for animal in animals: 
#     animal.speak()



######################## Aggregation 
# They are independent of each other



# class Library:

#     def __init__(self, name):
#         self.name =  name
#         self.books =  []


#     def add_book(self, book):
#         self.books.append(book)


#     def display_book(self):
#         return [print(book) for book in self.books]


#     def __str__(self):
#         return f"This is {self.name} library"

# class Book:
#     def __init__(self, title, author):
#         self.title =  title
#         self.author =  author


#     def __str__(self):
#         return f"{self.title} is written by {self.author} "



# # library =  Library("Unilorin")
# book1 = Book('The Fastest finger', "Rasheed Adeola")
# book2 = Book('Pain on trying', "Dolapo Kenny")

# print(book2)

# # library.add_book(book1)
# # library.add_book(book2)


# # library.display_book()

# # print(book1)



####### ------------------ Composition


# composition contains class call - the composed object directly owns its component, which cannot exist independently, owns a relationship
# class Engine:

#     def __init__(self, horse_power):
#         self.horse_power =  horse_power

# class Wheel:
#     def __init__(self, size):
#         self.size = size


# class Car:
#     def __init__(self, make, model, horse_power, wheel_size):
#         self.make = make
#         self.model =  model
#         self.engine = Engine(horse_power)
#         self.wheels =  [Wheel(wheel_size) for wheel in range(4)]

#     def display_car(self):
#         return f"{self.make} {self.model} {self.engine.horse_power}hp {self.wheels[0].size}in"


# car =  Car(make="Ford", model="Mustang", horse_power=500, wheel_size=18)


# print(car.display_car())



####### ------------------ Nested Classess


# class Company:

#     class Employee:
#         def __init__(self, name, position):
#             self.name =  name
#             self.position =  position

#         def get_details(self):
#             return f"This is {self.name} working as a {self.position}"
        
#     def __init__(self, company_name,):
#         self.company_name =  company_name
#         self.employees =  []

#     def add_employee(self, name, position):
#         new_employee =  self.Employee(name, position)
#         self.employees.append(new_employee)


#     def list_employees(self):
#         return [ employee_staff.get_details() for employee_staff in self.employees]

#     def __str__(self):
#         return f"This is {self.company_name} with {len(self.employees)}"


# company1 = Company('Agro-produce')

# company1.add_employee('Oladele', "Crop Engineer")
# company1.add_employee('kola', "pests Engineer")



# for employee in company1.list_employees():
#     print(employee)



####### ------------------ Static methods (utility methods)


# Static method - doesn't require access of class data



# class Employee:

#     def __init__(self, name, position,):
#         self.name =  name
#         self.position =  position


#     @staticmethod
#     def is_valid_position(position):
#         valid_position =  ['Cook', 'Manager', 'Waitresss']
#         return position in valid_position

#     def __str__(self):
#         return f"This is {self.name} with {len(self.position)}"


# company1 = Employee('Adeola', 'Manager')


# print(company1)

# print(Employee.is_valid_position('Goalkeeper'))


# ####################################  Class methods


# class Student:

#     count  =  0
#     total_gpa = 0

#     def __init__(self, name, gpa):
#         self.name =  name
#         Student.count += 1
#         Student.total_gpa += gpa

#     # Instance methos
#     def get_info(self):
#         return f"{self.name} has {self.total_gpa}"

#     # Class Method
#     @classmethod
#     def get_student_count(cls):
#         return f"We have {cls.count} graduating students this year "


#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count ==0:
#             return 0
#         else:
#             return f"Average gpa is {cls.total_gpa / cls.count:.2f}"
        


# student1 = Student('ola', 3.6)
# student2 = Student('ola', 4.0)
# student2 = Student('ola', 4.9)

# print(Student.get_student_count())
# print(student1.get_info())
# print(Student.get_average_gpa())





# ========================================== Dunder Methods

class Book:

    def __init__(self, title, author, pages):
        self.title =  title
        self.author =  author
        self.pages =  pages

    def __str__(self):
        return f" {self.author} wrote the book titled '{self.title}'"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


    def __lt__(self, other):
        return self.pages < other.pages

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'pages':
            return self.pages
        else:
            return 'key not found'

book1 = Book('Pain on trying', "Rasheed Adeola", 201)
book2 = Book('Pain on trying', "Dolapo Kenny,", 302)

# print(book1 == book2)
# print(book1.pages < book2.pages)
# print(book2['title'])
# print(book2['pages'])






# ========================================== Property Methods


# property method - Docorator used to dfine a method as a property 
# setters and getters - benefit - read, write or delete  attributes

# setters - for adding additional logic 


class Rectangle:

    def __init__(self, width, height):
        self._width =  width
        self._height =  height

    @property
    def width(self):
        return f"{self._width}"
    
    @property
    def height(self):
        return f"{self._height}"

    @width.setter
    def width(self, new_value):
        if new_value >  0:
            self._width = new_value
        else:
            print('Width Value Must be greater than zero ')

    @height.setter
    def height(self, new_value):
        if new_value >  0:
            self._height = new_value
        else:
            print('Height Value Must be greater than zero ')

    @width.deleter
    def widht(self):
        del self._width
        print(f"Width value {self.width} has been deleted ")

    @height.deleter
    def height(self):
        del self._height
        print(f"height value has been deleted ")

    @width.deleter
    def width(self):
        del self._width
        print(f"width value has been deleted ")



rectangle = Rectangle(30, 20)


# rectangle.width =  60
# rectangle.height =  0

del rectangle.width
del rectangle.height


print(rectangle.width)
print(rectangle.height)


        

