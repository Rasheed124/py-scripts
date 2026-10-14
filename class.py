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

num=10
res = num.__add__(5) 
print(res)