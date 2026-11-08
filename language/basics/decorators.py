# # metaprogramming

# # Add functionality to an existing function with decorators. This is called metaprogramming.

# # Decorator - A function that take a function as an argument

# def hello(func):
#     def inner():
#         print("Hello ")
#         func()
#     return inner

# def name():
#     print("Alice")


# # obj = hello(name)
# # obj()


# @hello
# def name():
#     print("Alice")

# if __name__ == "__main__":
#     name()




# def summed_decorator(func):

#     def inner(a, b):
#         print("Print Sum of a and b ")
#         return func(a, b)
#     return inner



# @summed_decorator
# def sum(a, b):
#     summed = a + b
#     print(summed)


# if __name__ == "__main__":
#     sum(5, 3)






# import time

# def measure_time(func):

#   def wrapper(*arg):
#       t = time.time()
#       res = func(*arg)
#       print("Function took " + str(time.time()-t) + " seconds to run")
#       return res

#   return wrapper

# @measure_time
# def myFunction(n):
#   time.sleep(n)

# if __name__ == "__main__":
#     myFunction(2)




# def sum(a , b):
#     print(f"Sum of a and b is: {a + b} ")

# sum(2, 5)

