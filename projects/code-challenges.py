


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


###### LEVEL 2

# def get_word_dic(word):

#     frequency = {}
#     # count = 0

#     for item in word:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1
#     return frequency

# print(get_word_dic("Programming"))


# Word Frequency — Given a sentence, return a dictionary containing how many times each word occurs. Ignore capitalization and basic punctuation.

# import string

# def remove_punctuation(sentence):
#     result = ""

#     for char in sentence:
#         if char not in string.punctuation:
#             result += char

#     return result


def remove_punctuation(sentence):

    non_characters = {',', '-', '@', '.', '!', '?', ':', ';'}

    result = ""

    for char in sentence:
        if char not in non_characters:
            result += char

    return result

def word_sentence_dic(sentence):

    word_dic = {}

    sentence_words  = remove_punctuation(sentence).replace(" ", "").lower()

    for word in sentence_words:
        if word in word_dic:
            word_dic[word]  += 1
        else:
            word_dic[word] = 1

    return word_dic

# print(word_sentence_dic("I like eating amala and okro fried-soup, with cold drinks"))



# Remove Duplicates While Preserving Order — [4, 2, 4, 1, 2, 8] should become [4, 2, 1, 8]. Don't simply convert the entire list to a set because order matters.


# def remove_duplicate(list):

#     new_list = []
#     for num in list:
#         if num not in new_list:
#             new_list.append(num)
#         else:
#             continue
#     return new_list

# print(remove_duplicate([4, 2, 4, 1, 2, 8]))


# def remove_duplicate(list):

#     list_dic = {}
#     for num in list:
#         if num in list_dic:
#             list_dic[num] += 1
#         else:
#             list_dic[num] = 1
#     return list_dic

# remove_duplicate([4, 2, 4, 1, 2, 8])




# Common Elements — Given two lists, return values occurring in both without duplicates. Solve it once using loops and once using sets.

# with loop

# with set
# def common_elements(list1, list2):

#     common_element = []
#     element2 = set(list2)

#     for num in list1:
#         if num in element2 and num not in common_element:
#             common_element.append(num)


#     return common_element

# print(common_elements([2, 4, 6, 8, 10, 4], [1, 3, 4, 6, 9, 10, 6]))


# Missing Number — You're given numbers from 1 to n, but exactly one number is missing. Example: [1, 2, 3, 5, 6] → 4. Try solving it without sorting first. Missing-number challenges are also common in Python challenge sets.



# def find_missing_number(lists):

#     new_num_list= []
#     missing_number = []

#     for key in range(lists[0], lists[-1]+1):
#         new_num_list.append(key)
#     for num in new_num_list:
#         if num not in lists:
#             missing_number.append(num)

#     return missing_number

# print(find_missing_number([1, 2, 3, 4, 5, 7, 8, 9, 10]))


#  **Second Largest Unique Number** — `[10, 5, 8, 10, 9] → 9`. Handle duplicates correctly.

# def cal_max(numbers) -> int:
#     highest_number =  numbers[0]
#     second_highest_number =  0

#     for number in numbers:
#         if number > highest_number:
#             highest_number = number
#         for number in numbers:
#             if number > second_highest_number and highest_number > number:
#                 second_highest_number = number

#     return second_highest_number
    
# print(cal_max([4, 12, 7, 25, 9, 18 ,100 ,30]))

# Split Even and Odd — Given a list of integers, return a dictionary such as {"even": [...], "odd": [...]}.
# def get_integer_dict(lists) -> dict:

#     integer_dict =  {'even': [], 'odd' : []}

#     for num in lists:
#         if num % 2 == 0 and num != 0:
#             integer_dict['even'].append(num)
#         elif num % 2 != 0 and num != 0:
#             integer_dict['odd'].append(num)
#         else:
#             continue
#     return integer_dict

# print(get_integer_dict([4, 12, 7, 25, 9, 18 ,100, 300, 1000, 0 ,30]))



# dict_one = {
#     "apple": 3,
#     "banana": 2,
#     "mango": 7,
#     "grape": 4
# }

# dict_two = {
#     "banana": 4,
#     "orange": 5,
#     "apple": 2,
#     "watermelon": 3
# }

# def merge_dictionaries(dict_one, dict_two):

#     merged_dic = {}

#     for key, value in dict_one.items():
#         merged_dic[key] = value
#         for key, value in dict_two.items():
#             if key not in  merged_dic:
#                 merged_dic[key] = value
#             else:
#                 continue
#     return merged_dic
        
      
# print(merge_dictionaries(dict_one=dict_one, dict_two=dict_two))





# Level 3 — Functions + Real Data Manipulation


students = [
    {"name": "Ada", "age": 22, "score": 88},
    {"name": "David", "age": 19, "score": 72},
    {"name": "bola", "age": 19, "score": 72},
    {"name": "Grace", "age": 24, "score": 95},
    {"name": "John", "age": 21, "score": 67},
    {"name": "Mary", "age": 20, "score": 88},
]


# Best Student — Return the dictionary representing the student with the highest score. Use max() with key= rather than manually looping.

# def sort_student_by_score(students):


#     student = max(students, key=lambda x: x['score'] )

#     return student

# print(sort_student_by_score(students=students))



# Youngest Student — Find the youngest student using min(key=...).

# def get_student_with_youngest_age(students):


#     student = min(students, key=lambda x: x['age'] )

#     return student

# print(get_student_with_youngest_age(students=students))



# Rank Students — Sort students from highest to lowest score. If two students have equal scores, sort those students alphabetically by name.

# def sort_student_by_score():

#     students.sort(key=lambda student: (-student['score'], student['name']))

#     return students


# print(sort_student_by_score())


# Passing Students — Return students with scores of at least 70. Solve once with a comprehension and once with filter()

# def get_Student_age_seventy():
    # result = [student for student in students if student['age'] <= 70 ]

    # print(result)
    # result = list(filter(lambda student: student['age'] <= 70, students))

    # return result

# print(get_Student_age_seventy())

# Extract Names — Convert the students into ["Ada", "David", ...] using map().

# def get_students_names():

#     result = list(map(lambda student: student['name'], students))

#     return result

# print(get_students_names())


# Everybody Passed? — Use all() to determine whether every student scored at least 50.

# def check_if_student_below_fifty():

#     return all(student['score'] <= 50 for student in students )

# print(get_student_below_fifty())

# Any Excellent Student? — Use any() to determine whether at least one student scored 90 or higher.

# def check_if_student_scored_90_or_higher():

#     return any(student['score'] >= 90 for student in students )

# print(check_if_student_scored_90_or_higher())


# Class Average — Calculate the average score. Then return all students whose scores are above that average.

# from functools import reduce

# import math

# def check_average_score():

#     total_score = list(map(lambda student: student['score'], students))
    
#     total_score = reduce(lambda x, y:  int(x) + int(y), total_score)

#     avg = math.floor(total_score / len(students))

#     required_students = list(filter(lambda student: student['score'] > avg, students))

#     return required_students

    
# print(check_average_score())



#################################################################   Level 4 — HOF Workout ############################################################

# Product Using reduce() — Given [2, 3, 4, 5], calculate 120 using reduce(). Then write the same operation using an ordinary loop and compare readability.

from functools import reduce

# def calc_total_items(numbers):

#     # result = reduce(lambda x, y: x + y, numbers)
#     # return result
#     result = 0

#     for num in numbers:
#         result += num
#     return result

# print(calc_total_items([2, 3, 4, 5]))


# Longest Word Using reduce() — Given ["cat", "elephant", "tiger", "hippopotamus"], use reduce() to determine the longest word.

# def calc_longest_word(words):

#     result = reduce(lambda x, y: x if len(x) > len(y) else y, words )
#     return result


# print(calc_longest_word(["cat", "elephant", "tiger", "hippopotamus"]))


# Clean and Transform — Given: Use filter() and map() to keep only positive even numbers and square them. Expected result: [64, 144, 400].

# numbers = [3, -1, 8, -5, 12, 7, 0, 20]

# def get_nums_and_square(numbers):

#     filtered_nums = list(filter(lambda num : num > 0 and num % 2 == 0, numbers))
#     result = list(map(lambda num : num ** 2, filtered_nums))

#     return result

# print(get_nums_and_square([3, -1, 8, -5, 12, 7, 0, 20]))


# Pair Names and Scores — Given:

# names = ["Ada", "David", "Grace"]
# scores = [88, 72, 95]


# def covert_to_dict(names, scores):

#     result = {}

#     for name, value in zip(names,scores):
#         result[name] = value
       
#     return result
# print(covert_to_dict(["Ada", "David", "Grace"], [88, 72, 95]))


# Indexed Ranking — Given names already sorted by score, use enumerate() to produce strings like "1. Grace", "2. Ada", "3. David"

# def indexed_ranking(names):

#     result = []
#     for index, name in enumerate(names, start=1):
#         value =  f"{index}, {name}"
#         result.append(value)
#     return result

# print(indexed_ranking( ["Grace", "Ada", "David", "Mary", "John"]))


# Original price:       1000
# Tax:                  7.5%
# Discount:             10%

from functools import partial

# tax_amount = discounted_price × tax_rate
def calculate_price(price, discount, tax_rate):

    discount_amount = float(f"{price * discount}")

    discounted_price = price - discount_amount

    tax_amount =  float(f"{discounted_price * tax_rate}")

    final_price = discounted_price + tax_amount

    return final_price

calc_tax_rate = partial(calculate_price, tax_rate=0.075)    
print(calc_tax_rate(1000, 0.10))




