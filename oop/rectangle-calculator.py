

# class Rectangle:

#     def __init__(self, width : int, height: int):

#         if not isinstance(width, (int, float)) or isinstance(width, bool):
#             raise TypeError("Width must be a numeric integer")
#         if not isinstance(height, (int, float)) or isinstance(height, bool):
#             raise TypeError("Height must be a numeric integer")

#         if width <=0:
#             raise ValueError("Width must be greater than zero")

#         if height <=0:
#             raise ValueError("Height must be greater than zero")
        
#         self.width =  width
#         self.height = height


#     def calculate_area(self):
#         area =  self.height * self.width
#         return area

#     def calculate_perimeter(self):
#         perimeter =   2 * (self.height + self.width)
#         return perimeter

#     def display_details(self):
#         print(f"DImenntion details ")
#         print(f"Area is : {self.area}")
#         print(f"Perimeter is : {self.perimeter}")
#         print(self.check_if_rectangle_is_a_Square())
    
#     @property
#     def perimeter(self):
#         perimeter =   2 * (self.height + self.width)
#         return perimeter

#     @property
#     def area(self):
#         area =  self.height * self.width
#         return area
    

#     def check_if_rectangle_is_a_Square(self):
#         return "Is a square" if self.width ==  self.height else "Not a square"


#     def __gt__(self, other):
#         return self.area > other.area

#     def __str__(self):
#         return f"Calculating the are and perimeter of a Rectangle"


# rectangle1 = Rectangle(30, 50)
# rectangle2 = Rectangle(20, 50)
# rectangle3 = Rectangle(True, 0)

# print(rectangle2.check_if_rectangle_is_a_Square())
# print(rectangle1 > rectangle2)

# print(rectangle2.display_details())
# print(rectangle3.display_details())








# ==================== AI REVIEW


class Rectangle:

    def __init__(self, width: int | float, height: int | float):

        if not isinstance(width, (int, float)) or isinstance(width, bool):
            raise TypeError("Width must be numeric.")

        if not isinstance(height, (int, float)) or isinstance(height, bool):
            raise TypeError("Height must be numeric.")

        if width <= 0:
            raise ValueError("Width must be greater than zero.")

        if height <= 0:
            raise ValueError("Height must be greater than zero.")

        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    @property
    def area(self):
        return self.calculate_area()

    @property
    def perimeter(self):
        return self.calculate_perimeter()

    def is_square(self):
        return self.width == self.height

    def display_details(self):
        square_status = "Yes" if self.is_square() else "No"

        return (
            f"Width: {self.width}\n"
            f"Height: {self.height}\n"
            f"Area: {self.area}\n"
            f"Perimeter: {self.perimeter}\n"
            f"Is square: {square_status}"
        )

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented

        return self.area > other.area

    def __str__(self):
        return (
            f"Rectangle(width={self.width}, "
            f"height={self.height})"
        )


# 1. Create three valid rectangles
rectangle1 = Rectangle(30, 50)
rectangle2 = Rectangle(20, 50)
rectangle3 = Rectangle(25, 25)

# 2. Display details
print("--- Rectangle 1 ---")
print(rectangle1.display_details())

print("\n--- Rectangle 2 ---")
print(rectangle2.display_details())

print("\n--- Rectangle 3 ---")
print(rectangle3.display_details())

# # 3. Test square detection
# print("\n--- Square Tests ---")
# print(rectangle1.is_square())  # False
# print(rectangle3.is_square())  # True

# # 4. Test area and perimeter
# print("\n--- Calculations ---")
# print("Rectangle 1 area:", rectangle1.calculate_area())        # 1500
# print("Rectangle 1 perimeter:", rectangle1.calculate_perimeter())  # 160

# # 5. Compare rectangles by area
# print("\n--- Area Comparison ---")
print(rectangle1 > rectangle2)  # True
# print(rectangle2 > rectangle1)  # False

# # 6. Test object independence
# print("\n--- Independence Test ---")
# print("Rectangle 1 width before:", rectangle1.width)
# print("Rectangle 2 width before:", rectangle2.width)

# rectangle1.width = 100

# print("Rectangle 1 width after:", rectangle1.width)  # 100
# print("Rectangle 2 width after:", rectangle2.width)  # 20

# # 7. Test invalid dimensions
# print("\n--- Validation Tests ---")

invalid_rectangles = [
    ("Negative width", -5, 10),
    ("Zero height", 10, 0),
    ("Boolean width", True, 10),
    ("Text height", 10, "large"),
]

for test_name, width, height in invalid_rectangles:
    try:
        Rectangle(width, height)
    except (TypeError, ValueError) as error:
        print(f"{test_name}: {type(error).__name__}: {error}")

# 8. Test string representation
print("\n--- String Representation ---")
print(rectangle1)
