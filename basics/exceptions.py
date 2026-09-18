# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

# number = 10
# assert number <= 5, f"The number should not exceed 5. ({number=})"
# print(number)




def linux_interaction():
    import sys
    if "linux" not in sys.platform:
        raise PlatformException("Function can only run on Linux systems.")
    print("Doing Linux things.")



# def linux_interaction():
#     import sys
#     if "linux" not in sys.platform:
#         raise RuntimeError("Function can only run on Linux systems.")
#     print("Doing Linux things.")

# ...


# try:
#     # linux_interaction()
#     with open("file.log") as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except RuntimeError as error:
#     print(error)
#     print("Linux linux_interaction() function wasn't executed.")



    # ...

# try:
#     linux_interaction()
# except RuntimeError as error:
#     print(error)
# else:
#     print("Doing even more Linux things.")

### Proceeding After a Successful Try With else


# ...

# try:
#     linux_interaction()
# except RuntimeError as error:
#     print(error)
# else:
#     print("Doing even more Linux things.")



# Cleaning Up After Execution With finally

try:
    linux_interaction()
except RuntimeError as error:
    print(error)
else:
    try:
        with open("file.log") as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print("Cleaning up, irrespective of any exceptions.")





#### Creating Custom Exceptions in Python


# class PlatformException(Exception):
#     """Incompatible platform."""


# def linux_interaction():
#     import sys
#     if "linux" not in sys.platform:
#         raise PlatformException("Function can only run on Linux systems.")
#     print("Doing Linux things.")



# linux_interaction()