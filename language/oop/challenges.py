
class Student:

    adult_age = 18

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def get_students_details(self):
        return f"{self.name} is {self.age} years old and studies {self.course}"

    def check_student_is_adult(self):
        return "You are an adult" if self.age >= Student.adult_age else "You are not an adult"


student1 = Student("Rasheed", 30, "Mathematics")
student1.name = "Habeeb"

student2 = Student("Adeola", 17, "Physics")

student3 = Student("Fatima", 20, "Computer Science")

# print(student1.get_students_details())
# print(student1.check_student_is_adult())

# print(student2.get_students_details())
# print(student2.check_student_is_adult())

# print(student3.get_students_details())
# print(student3.check_student_is_adult())

# # Demonstrate independent object state
# print("\nBefore changing student1's name:")
# print("Student 1:", student1.name)
# print("Student 2:", student2.name)

# student1.name = "Ibrahim"

# print("\nAfter changing student1's name:")
# print("Student 1:", student1.name)
# print("Student 2:", student2.name)













    
        



