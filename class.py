# class SampleClass:
#     def __init__(self, value):
#         self.__value = value

#     def __method(self):
#         print(self.__value)

#     def display(self):
#         self.__method()


# obj = SampleClass("Hello")
# print(vars(obj))

# vars(SampleClass)
# obj.display()  


# class ObjectCounter:
#     num_instances = 0
#     def __init__(self):
#         type(self).num_instances += 1



# obj = ObjectCounter()

# print(obj.num_instances)

# num=10
# res = num.__add__(5) 
# print(res)



# name = "expense name".split()
# name = "_".join(name)

# print(name)

from pathlib import Path

DATA_DIR = Path(__file__).parent
filename = input("Enter filename: ")

DATA_FILE = DATA_DIR / filename

if DATA_FILE.is_file():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        # Process file
        pass
else:
    print("File not found in the working folder.")