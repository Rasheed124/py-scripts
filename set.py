# A = {1, 2, 3, 4, 5}
# B = {1, 2, 4}
 
# print(A.issuperset(B))
# # Output: True
 
# print(B.issubset(A))
# # Output: True



# Creating and Manipulating Sets in Python



S1 = {1, 2, 3}
S2 = S1.copy()  # independent copy of S1
S1.clear()
 
print(S1)
# Output: set()
 
print(S2)
# Output: {1, 2, 3}


# Where Can You Use Python Sets?


# A common example is to remove duplicates from a list by transforming it into a set and back into a list:

values = [1, 2, 2, 1, 3, 4, 1, 2, 3, 4, 1]
unique_values = list(set(values))
 
print(unique_values)
# Output: [1, 2, 3, 4]

# Another common application for sets is filtering data. Let’s say that you have three lists of IDs: one of all of your clients, and two others of clients who bought product X or Y: