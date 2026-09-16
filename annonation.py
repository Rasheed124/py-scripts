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

print(result)



# MutableMapping
