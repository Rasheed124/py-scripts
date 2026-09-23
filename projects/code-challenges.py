


# def is_even(n):
#     return True if n % 2 == 0 else False

# def analyze_number(n):
#     if n < 0:
#         return "negative even" if is_even(n) else "negative odd"
#     elif n > 0:
#         return "positive even" if is_even(n) else "positive odd"
#     else:
#         return "Xero"


# print(analyze_number(0))



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
    

# def get_occurence_number(numbers, num):

#     count_occurence = 0

#     for i in numbers:
#          if num == i:
#               count_occurence += 1

#     return count_occurence


# print(get_occurence_number([4, 2, 7, 4, 2, 4, 9], 4))


    # frequency = {}
    # heighest_count = 0

    # for number in numbers:
    #     if number in frequency:
    #         frequency[number] += 1
    #     else:
    #         frequency[number] = 1

    # for item in frequency:
    #     if frequency[item] > heighest_count:
    #         heighest_count = frequency[item]
    # return heighest_count

# print(get_occurence_number([4, 2, 7, 4, 2, 4, 9], 4))




# Reverse a String — Reverse a string without using [::-1] or reversed().


# def reversed_string(string):
#     new_char = ""
#     for key, _ in enumerate(string, start=1):
#         new_char += string[-key]
#     return new_char
       
# print(reversed_string("adeola"))


# Palindrome Checker — Determine whether a string reads the same forward and backward. Ignore capitalization and spaces. For example, "Never odd or even" should return True.


# def is_palindrom_passed(string):
#     formatted_string =  string.replace(" ", "").lower()
#     forward_string , backward_string = "", ""
#     for key, _ in enumerate(formatted_string):
#         forward_string += formatted_string[key]
#     for key, _ in enumerate(formatted_string, start=1):
#         backward_string += formatted_string[-key]

#     return True if forward_string == backward_string else False

    
# print(is_palindrom_passed("Never odd or even"))


# FizzBuzz Extended — For numbers 1–100: multiples of 3 → "Fizz", 5 → "Buzz", 3 and 5 → "FizzBuzz". Add another rule: multiples of 7 → "Bang". If multiple rules apply, combine the words.



# def check_fizzBuzz(num):

#     for integer in range(1, num+1):

#         answer = ""

#         if integer % 3 == 0:
#             answer += "Fizz"

#         if integer % 5 == 0:
#             answer += "Buzz"

#         if integer % 7 == 0:
#             answer += "Bang"

#         if answer:
#             print(answer)
#         else:
#             print(integer)


# check_fizzBuzz(100)