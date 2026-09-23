# import mod


# print(mod.s)



# from mod import s, foo
# s

# # foo('quux')



# from mod import *
# s

# a

# foo

# Foo

# from mod import s as str_statement

# print(str_statement)



# import mod as my_module
# my_module.a

# my_module.foo('qux')


# try:
#     import mod
# except ImportError:
#     print("Module not found")


# dir function - The built-in function dir() returns a list of defined names in a namespace. 

# import mod
# print(dir(mod))


# Executing a Module as a Script - fact
from fact import fact

print(fact(5))



# Reloading a Module


import mod


import mod

import importlib
importlib.reload(mod)


# Python Packages

# from pkg import mod1
# mod1.foo()


# from pkg import mod2 as quux
# quux.bar()


# Package Initializationz

# If a file named __init__.py is present in a package directory, it is invoked when the package or a module in the package is imported. This can be used for execution of 
# package initialization code, such as initialization of package-level data.

# >>> import pkg
# Invoking __init__.py for pkg
# >>> pkg.A
# ['quux', 'corge', 'grault']




# Importing * From a Package - second part part of package initializar



# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
# '__package__', '__spec__']

# >>> from pkg import *
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
# '__package__', '__spec__']


# Second option inside a module itself

# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
# '__package__', '__spec__']

# >>> from pkg.mod1 import *
# >>> dir()
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__',
# '__package__', '__spec__', 'foo']

# >>> foo()
# [mod1] foo()
# >>> Foo
# Traceback (most recent call last):
#   File "<pyshell#37>", line 1, in <module>
#     Foo
# NameError: name 'Foo' is not defined