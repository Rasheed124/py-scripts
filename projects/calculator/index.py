# a = [1, 4, 5]
# b = [1, 4, 5]


# print(b is a)

# name = "Rasheed"

# print(f"My name {name} is {len(name)} characters long")

# input_var_Str =  input("Enter some data: ")

# print(f"{'correct' if input_var_Str == 'ade' else 'incorrect'}")


# other_list = [1, 4, 5, 8]

# li.append(other_list)
# li.pop()

li = [1, 2, 3]
li2 = [4, 5, 6]

# li2 =  li[:]

# print(li.index(0))


# print(li.insert(2, [0,1, 0]))

# print(li)

# li.extend(li2)

# print(3 in li)



# TUPLE
filled_dict = {"one": 1, "two": 2, "three": 3}

# if "one" in filled_dict:
#     print("correct key")
# else:
#     print("incorrect key")


# print(filled_dict['four'])

# print(filled_dict.get('ones', 1))

# invalid_dict = {[1,2,3]: "123"}  # => Yield a TypeError: unhashable type: 'list'
# valid_dict = {(1,2,3):[1,2,3]} 

# print(invalid_dict)

# print(list(filled_dict.keys()))

# print("one" in filled_dict)

# print(resut)



# age =  {"age" : 20}
# a = { "name" :  "ola", **{"age" : 20}}

# print(a)


students = {"ade", "ola", "bola", "shola"}
paid_students = { "ola", "bola"}


# for student in students:
#     print(student)




# command = "123"

# match command:
#     case "run":
#         print("The robot started to run 🏃‍♂️")
#     case "speak" | "say_hi":  # multiple options (OR pattern)
#         print("The robot said hi 🗣️")
#     case code if command.isdigit():  # conditional
#         print(f"The robot execute code: {code}")
#     case _:  # _ is a wildcard that never fails (like default/else)
#         print("Invalid command ❌")







animals=  ["dog", "cat", "mouse"]

# for animal in animals:
#     # You can use format() to interpolate formatted strings
#     print("{} is a mammal".format(animal))
#     # print(f"{animal} is a mammal")




# for key, value in enumerate(animals):
#     print(key)



# try:
#     # Use "raise" to raise an error
#     raise IndexError("This is an index error")
# except IndexError as e:
#     pass                 # Refrain from this, provide a recovery (next example).
# except (TypeError, NameError):
#     pass                 # Multiple exceptions can be processed jointly.
# else:                    # Optional clause to the try/except block. Must follow    # all except blocks.
#     print("All good!")   # Runs only if the code in try raises no exceptions
# finally:                 # Execute under all circumstances
#     print("We can clean up resources here")

# from pathlib import Path
# import json
# # Getting content inside a file

# contents = {"aa": 12, "bb": 20}

# file_path = Path(__file__).parent / "index.txt"

# # with open(file_path, 'w') as f:
# #      f.write(json.dumps(contents))
#     #  f.write(str(contents))


# with open(file_path, "r") as file:
#     contents = json.load(file)
# #     # contents = file.read()
# print(contents)


# filled_dict = {"one": 1, "two": 2, "three": 3}

# iterable = iter(filled_dict.values())

# print(iterable)

# for key in iterable:
#     print(key)



def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 =  create_adder(10)

# print(add_10())
# print(add_10(4))


# def calculation_user_age(name):

#     def show_user_info(age):
#         print(f"Good morning {name}, you are {age} year old")
#     return show_user_info

# get_user_info =  calculation_user_age("Adeola")

# print(get_user_info(20))


def create_avg():
    total = 0
    count= 0
    def avg(n):
        nonlocal  total, count
        total += n
        count += 1
        return total/count
    return avg


avg =  create_avg()
# print(avg(3))  # => 3.0
# print(avg(5))  # (3+5)/2 => 4.0
# print(avg(7))  # (8+7)/3 => 5.0


value = (lambda x : x >2)(2)

# print(value )



students = [
    ("John", 25),
    ("Mary", 19),
    ("David", 22),
]



students.sort(key=lambda student: student[1])


students = [
    ("John", 25),
    ("Mary", 19),
    ("David", 22),
]

students.sort(key=lambda student: student[1])

# print(students)
items =  [1, 2, 3, 4, 5, 6, 7]
map_result = map(add_10, items) 
filter_result = map(add_10, items)
# print( list(map_result))       
# print( list(filter_result))       
# list(map(max, [1, 2, 3], [4, 2, 1])) 



# print([x for x in [1, 2, 3, 4, 5, 6, 7] if x > 2 ])

# result = []

# for i in [1, 2, 3, 4, 5, 6, 7]:
#     if i > 2:
#         result.append(i)

# print("new list {}".format(i))

# value = {x  for x in "abcdefghi" if x not in "abc"}

# print(value)


# HOFs

# students = [
#     ("John", 25),
#     ("Mary", 19),
#     ("David", 22),
# ]


numbers = [10, 3, 7, 2, 8, 5]

students = [
    ("John", 25),
    ("Mary", 19),
    ("David", 22),
    ("Sarah", 30),
]

products = [
    ("Laptop", 850),
    ("Phone", 500),
    ("Tablet", 300),
    ("Monitor", 700),
]

expensive_prod  =  max(products, key=lambda product: product[1])
cheapest_prod  =  min(products, key=lambda product: product[1])

# print(expensive_prod)
# print(cheapest_prod)
# print(st)

# ANY and all

numbers = [12, 7, 3, 20, 15]


# products = ["Laptop", "Phone", "Tablet"]
# prices = [850, 500, 300]



names = ["John", "Mary", "David", "Sarah"]
scores = [85, 92, 78, 95]


merged_products = dict(zip(names, scores))
# merged_products = list(zip(products, prices))

# print(merged_products)

# for prod, items in merged_products.items() :
#     print("{} cost {}".format(prod, items))

students = ["John", "Mary", "David", "Sarah"]


# for key, student in enumerate(students, start=1):
#     print(f"{key}. {student}")


from functools import  partial


# numbers = [2, 4, 6, 8, 10]


# numbers = [3, 8, 11, 14, 17, 20, 25]

numbers = [2, 3, 4, 5]


# result = list(map(lambda x : x* 3 , numbers  ))
# print(result)


# result = list(filter(lambda x : x >10 , numbers  ))

# result = reduce(lambda a, b: a * b, numbers )

# print(result)


# result = any(i > 18 for i in numbers)
# result = all(i > 0 for i in numbers)

# if result:
#     print("Yes")


# def power(base, exponent):
#     return base ** exponent

# def multiply(a, b):
#     return a * b


# multiply_by_10 = partial(multiply, b=10)

# print(multiply_by_10(5))
# print(multiply_by_10(8))
# print(multiply_by_10(12))

    

from operator import itemgetter

students = [
    ("John", 25),
    ("Mary", 19),
    ("David", 22),
    ("Sarah", 30),
]


# from operator import itemgetter

# student = ("John", 25, "Python")

# get_info = itemgetter(0, 2)

# print(get_info(student))

# result = sorted(students, key=itemgetter(1))

# print(result)



# from functools import cache, lru_cache


# @lru_cache(maxsize=3)
# def square(n):
#     print("Calculating...")
#     return n * n


# print(square(5))
# print(square(5))
# print(square(5))
# print(square(5))
# print(square(5))
# print(square(5))



