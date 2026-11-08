
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    @property
    def name(self):
        return self.__name

    @property
    def color(self):
        return self.__color



    @abstractmethod
    def area(self):
        """All Shapes must have an area to calculate"""
        pass

    def describe_properties(self):
        return (
            f"Name: {self.name}, "
            f"Color: {self.color}, "
        )


class Circle(Shape):
    def __init__(self, name, color, radius):
        super().__init__(name, color)

        self.__radius =  radius

    @property
    def radius(self):
        return self.__radius

    def area(self):
        area =  3.142 * self.radius**2
        return area


class Rectangle(Shape):
    def __init__(self, name, color, width, length):
        super().__init__(name, color)

        self.__width =  width
        self.__length =  length

    @property
    def width(self):
        return self.__width
    @property
    def length(self):
        return self.__length

    def area(self):
        area =  self.length * self.width
        return area

    
class Triangle(Shape):
    def __init__(self, name, color, base, height):
        super().__init__(name, color)

        self.__base =  base
        self.__height =  height

    @property
    def base(self):
        return self.__base

    
    @property
    def height(self):
        return self.__height

    def area(self):
        area =  (1/2) * self.base * self.height
        return area




# Create shape objects
circle = Circle("Plain Circle", "Grey", 30)

rectangle = Rectangle("Long Rectangle", "Blue", 30, 50)

triangle = Triangle("Triangle", "Red", 20, 15)


# Store objects of different classes in one list
shapes = [circle, rectangle, triangle]


# Test polymorphism
for shape in shapes:
    print(shape.describe_properties())
    print(f"Area: {shape.area()}")
    print("-" * 30)