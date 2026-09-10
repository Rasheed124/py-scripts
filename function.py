# TO DEFINE EMPTY FUNCTION


# def function():
#     pass

# function()


def calculate_cost(item="bananas", quantity=6, price=0.74):
    print(f"{quantity} {item} cost ${quantity * price:.2f}")

# calculate_cost("bananas", 0.74, 6)
# calculate_cost(price=0.74, quantity=6, item="bananas")


# calculate_cost("bananas", quantity=6, price=0.74)



# Returning Values


def as_dict():
     return dict(one=1, two=2, three=3)

print(as_dict()["two"])
# {'one': 1, 'two': 2, 'three': 3}

# >>> as_dict()["two"]
# 2



# def find_user(username, user_list):
#      for user in user_list:
#          if user["username"] == username:
#              return user
#      return None

# users = [
#     {"username": "alice", "email": "alice@example.com"},
#     {"username": "bob", "email": "bob@example.com"},
# ]

# find_user("alice", users)




# from pathlib import Path

# def read_file_contents(file_path):
#     path = Path(file_path)

#     if not path.exists():
#         print(f"Error: The file '{file_path}' does not exist.")
#         return

#     if not path.is_file():
#         print(f"Error: '{file_path}' is not a file.")
#         return

#     return path.read_text(encoding="utf-8")


# result = read_file_contents("test.txt")

# print(result)







# OPERATOR

# the is and is not operators.



# Returning Generator Iterators


def cumulative_average(numbers):
     total = 0
     for items, number in enumerate(numbers, 1):
         total += number
         yield total / items


values = [5, 3, 8, 2, 5]  # Simulates a large data set

for cum_average in cumulative_average(values):
     print(f"Cumulative average: {cum_average:.2f}")

# Cumulative average: 5.00
# Cumulative average: 4.00
# Cumulative average: 5.33
# Cumulative average: 4.50
# Cumulative average: 4.60