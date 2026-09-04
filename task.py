# ---------------------  FIRST ONE -------------------------------


# fullName = input("What's your name: ")
# dOB = input("What's Date of Birth: ")
# height = input("Your height in meters: ")
# favouriteColor = input("Your favourite color: ")

# print(f'''
# --- User Profile ---
# Name: {fullName}
# Date of Birth: {dOB}
# Height: {height}m
# Favorite Color: {favouriteColor}
# ''')

# ---------------------  Second  ONE -------------------------------

# firstNum = float(input("Enter first number: "))
# secondNum = float(input("Enter Second number: "))

# result = firstNum + secondNum

# print(f'''

# --- SUM Calculation----
# The Totoal score is {result} 


# ''')

# ---------------------  Third  ONE -------------------------------


# --------------------- Simple Interest & Budget Evaluator

# principal = float(input("Enter principal: "))
# rate = float(input("Enter rate: "))
# time = float(input("Enter time in years: "))

# interest = (principal * rate * time) / 100

# if interest > 500:
#     print("High Return")
# else:
#     print("Standard Return")

# print(f"Calculated Interest: ${interest}")


# ---------------------  Grade & Eligibility System

# score = float(input("Enter student score (0-100): "))
# attendance = float(input("Enter attendance percentage (0-100): "))

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# else:
#     grade = "F"

# if score >= 70 and attendance >= 75:
#     status = "Passed"
# else:
#     status = "Failed"

# print(f"Grade: {grade}")
# print(f"Status: {status}")



# ---------------------  Fifth  ONE -------------------------------




# --------------------- Number Guessing Game
secret_number = 7

for i in range(3):
    user_input = input("Guess the number: ")

    try:
        num_ber = float(user_input)
    except ValueError:
        print("Please enter a valid number!")
        continue
    
    
    if num_ber < secret_number:
        print("The guessed number is low, try again.")
    elif num_ber > secret_number:
        print("The guessed number is high, try again.")
    else:
        print("You win!")
        break
else:
    print("Game over! You ran out of attempts.")



# USING FOR LOOP

# secret_number =  7
# i =0
# while i < 3:
#     user_input = input("Guess the number: ")

#     try:
#         num_ber = float(user_input)
#     except ValueError:
#         print("Please enter a valid number!")
#         continue

#     i+=1

    
#     if num_ber < secret_number:
#         print("The guessed number is low, try again.")
#     elif num_ber > secret_number:
#         print("The guessed number is high, try again.")
#     else:
#         print("You win!")
#         break
# else:
#     print("Game over! You ran out of attempts.")