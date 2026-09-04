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


principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time in years: "))

interest = (principal * rate * time) / 100

if interest > 500:
    print("High Return")
else:
    print("Standard Return")

print(f"Calculated Interest: ${interest}")




score = float(input("Enter student score (0-100): "))
attendance = float(input("Enter attendance percentage (0-100): "))

# Assign Grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

# Check Pass/Fail Eligibility
if score >= 70 and attendance >= 75:
    status = "Passed"
else:
    status = "Failed"

print(f"Grade: {grade}")
print(f"Status: {status}")



# ---------------------  Fifth  ONE -------------------------------
