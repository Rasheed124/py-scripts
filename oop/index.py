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

from abc import ABC, abstractmethod


class Vechicle(ABC):

    @abstractmethod
    def go(self):
        pass


    @abstractmethod
    def stop(self):
        pass



class Car(Vechicle):
    def go(self):
        print("it can drive ")

    def stop(self):
        print("it can stop")


car =  Car()



######################## Super With Inheritance method



class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled


    def describe(self):
        print(f"It is {self.color} and {'is filled' if self.is_filled else  'is not filled'}")


class Rectangle(Shape):

    def __init__(self, color, is_filled, side):
        super().__init__(color, is_filled)
        self.side = side

    def describe(self):
        print(f"The area is {self.side * 2} cm2 ")
        return super().describe()


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius



circle =  Circle(color="Blue", is_filled=True, radius=20)
rectangle =  Rectangle(color="White", is_filled=False, side=20)

rectangle.describe()




######################## Polymorphism 
