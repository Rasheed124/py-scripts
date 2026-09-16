# def show_type(num):
#     if(isinstance(num, str)):
#         print("You entered a string")
#     elif (isinstance(num, int)):
#         print("You entered an integer")

# show_type('hello') # You entered a string
# show_type(3)       # You entered an integer





# Adding type hints to dictionaries

person = { "first_name": "John", "last_name": "Doe"}

person: dict[str, str] = { "first_name": "John", "last_name": "Doe"}

# print(person["first_name"])


# For function parameters, it recommends using these abstract base classes:

# Mapping


# 
# __getitem__: for accessing an element
# __iter__: for iterating
# __len__: computing the length
# 
# 

from collections.abc import Mapping

def get_full_name(student: Mapping[str, str]) -> str:
    return f'{student.get("first_name")} {student.get("last_name")}'

john = {
  "first_name": "John",
  "last_name": "Doe",
}

result = get_full_name(john)

# print(result)



# MutableMapping



from collections.abc import MutableMapping

def update_first_name(student: MutableMapping[str, str], first_name: str) -> None:
    student["first_name"] = first_name

john = {
    "first_name": "John",
    "last_name": "Doe",
}

update_first_name(john, "james")

# print(john)



# Using the TypedDict class as a type hint


from typing import TypedDict

class StudentDict(TypedDict):
    first_name: str
    last_name: str
    age: int
    hobbies: list[str]


def get_full_name(student: StudentDict) -> str:
    return f'{student.get("first_name")} {student.get("last_name")}'


student1: StudentDict = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 18,
    "hobbies": ["singing", "dancing"],
}


result  = get_full_name(student1)

# print(result)



# Adding type hints to tuples



from typing import NamedTuple

class StudentTuple(NamedTuple):
    name: str
    age: int

john = StudentTuple("John Doe", 33)


def student_info(student: StudentTuple) -> None:
    name, age = student
    print(f"Name: {name}\nAge: {age}")

student_info(john)




# Creating and using protocols

# __init__ is a special Python method.

# It is automatically called when you create an instance of the class.

from typing import Protocol

class HasBirthYear(Protocol):
    def get_birthyear(self) -> int:
        return self.birthyear

class Person:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear

    def get_birthyear(self) -> int:
        return self.birthyear

def calc_age(current_year: int, data: HasBirthYear) -> int:
    return current_year - data.get_birthyear()

john = Person("john doe", 1996)
print(calc_age(2021, john))


# Annotating overloaded functions