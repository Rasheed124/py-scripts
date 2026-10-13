

class Rectangle:

    def __init__(self, width : int, height: int):

        if not isinstance(width, (int, float)) or isinstance(width, bool):
            raise TypeError("Width must be a numeric integer")
        if not isinstance(height, (int, float)) or isinstance(height, bool):
            raise TypeError("Height must be a numeric integer")

        if width <=0:
            raise ValueError("Width must be greater than zero")

        if height <=0:
            raise ValueError("Width must be greater than zero")
        
        self.width =  width
        self.height = height


    def area(self):
        area =  self.height * self.width
        return f"Area is {area}cmSq"

    def __str__(self):
        return f"Calculating the are and perimeter of a Rectangle"


rectangle1 = Rectangle(30, 50)

print(rectangle1.area())