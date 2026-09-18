

# ========================================== Set Difference ======================================== #
# ========================================== Set Symmetric Difference ======================================== #

# The set symmetric difference operator returns the elements that are unique to either A or B, ignoring the elements that are common to both sets.

A = {1, 2, 4, 6, 8}
B = {1, 2, 3, 4, 5}
 
print(A.symmetric_difference(B))
 
# Output:
# {3, 5, 6, 8}


# ========================================== Supersets, Subsets, and Membership Using Python Sets ======================================== #


# A = {1, 2, 3, 4, 5}
# B = {1, 2, 4}
 
# print(A.issuperset(B))
# # Output: True
 
# print(B.issubset(A))
# # Output: True


# ========================================== Creating and Manipulating Sets in Python ======================================== #

S = set()
 
S.add(2)
print(S)
# Output: {2}
 
S.remove(2)
print(S)
# Output: set()

S1 = {1, 2, 3}
S2 = S1.copy()  # independent copy of S1
S1.clear()
 
print(S1)
# Output: set()
 
print(S2)
# Output: {1, 2, 3}


# ========================================== Where Can You Use Python Sets? ======================================== #


# A common example is to remove duplicates from a list by transforming it into a set and back into a list:

values = [1, 2, 2, 1, 3, 4, 1, 2, 3, 4, 1]
unique_values = list(set(values))
 
print(unique_values)
# Output: [1, 2, 3, 4]

# Another common application for sets is filtering data. Let’s say that you have three lists of IDs: one of all of your clients, and two others of clients who bought product X or Y:


all_clients = {104, 203, 255, 289, 448}
clients_bought_X = {104, 448}
clients_bought_Y = {104, 255, 289}



# Let’s try answering the following questions:

# Which clients bought product X and did not buy product Y?
# Which clients bought both products?
# Which clients bought nothing?


all_clients = {104, 203, 255, 289, 448}
clients_bought_X = {104, 448}
clients_bought_Y = {104, 255, 289}
 
# Question 1
print(clients_bought_X.difference(clients_bought_Y))
# Output: {448}
 
# Question 2
print(clients_bought_X.intersection(clients_bought_Y))
# Output: {104}
 
# Question 3
purchasers = clients_bought_X.union(clients_bought_Y)
print(all_clients.difference(purchasers))
# Output: {203}