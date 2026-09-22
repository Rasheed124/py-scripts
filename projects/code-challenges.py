


# # def is_even(n):
# #     return True if n % 2 == 0 else False


# # def analyze_number(n):
# #     if n < 0:
# #         return "negative even" if is_even(n) else "negative odd"
# #     else:
# #         return "positive even" if is_even(n) else "positive odd"


# # print(analyze_number(-6))


# 2. Largest Without max() — Write a function that receives a list of numbers and returns the largest number. Do not use max() or sorted().

# def cal_max(numbers) -> int:
#     highest_number =  numbers[0]

#     for number in numbers:
#         if number > highest_number:
#             highest_number = number
#     return highest_number
    
# print(cal_max([4, 12, 7, 25, 9, 18]))

# 3. Smallest Without min() — Same idea, but return the smallest value without min() or sorting.


# def cal_min(numbers) -> int:
#     lowest_number =  numbers[0]

#     for number in numbers:
#         if number < lowest_number:
#             lowest_number = number
#     return lowest_number
    
# print(cal_min([4, 12, 7, 25, 9, 18]))




# 4 Manual Sum — Write a function that calculates the sum of a list without sum()

# def cal_sum(numbers) -> int:
#     total_sum = 0

#     for number in numbers:
#         total_sum += number
    
#     return total_sum
    
# print(cal_sum([1, 3, 6]))



# Count Occurrences — Given [4, 2, 7, 4, 2, 4, 9] and 4, return 3. Don't use .count().
    

# def get_occurence_number(numbers):

#     frequency = {}
#     heighest_count = 0

#     for number in numbers:
#         if number in frequency:
#             frequency[number] += 1
#         else:
#             frequency[number] = 1

#     for item in frequency:
#         if frequency[item] > heighest_count:
#             heighest_count = frequency[item]
#     return heighest_count



# print(get_occurence_number([4, 2, 7, 4, 2, 4, 9]))




# Reverse a String — Reverse a string without using [::-1] or reversed().


def reversed_string(string):
    new_char = ""
    for key, _ in enumerate(string, start=1):
        new_char += string[-key]
    return new_char
       
print(reversed_string("adeola"))

