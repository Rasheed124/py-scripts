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
# secret_number = 7

# for i in range(3):
#     user_input = input("Guess the number: ")

#     try:
#         num_ber = float(user_input)
#     except ValueError:
#         print("Please enter a valid number!")
#         continue
    
    
#     if num_ber < secret_number:
#         print("The guessed number is low, try again.")
#     elif num_ber > secret_number:
#         print("The guessed number is high, try again.")
#     else:
#         print("You win!")
#         break
# else:
#     print("Game over! You ran out of attempts.")



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






# ---------------------  Multiplication Table & Filter

# user_input = input("Put your number: ")


# try:
#     num_ber = int(user_input)
    
#     for num in range(1, 13): 
#         result = num_ber * num
        
#         if result % 5 == 0:  
#             continue
            
#         print(f"{num_ber} x {num} = {result}")

# except ValueError:
#     print("Please enter a valid number!")





# --------------------- Dynamic Shopping Cart

# cart = []

# while True:
#     print("\n--- Shopping Cart Menu ---")
#     print("1. Add Item")
#     print("2. Remove Item")
#     print("3. Display Sorted Cart")
#     print("4. Quit")

#     choice = input("Choose an option (1-4): ").strip()

#     if choice == "1":
#         item = input("Enter item to add: ").strip()
#         if item.lower() in [i.lower() for i in cart]:
#             print(f"'{item}' is already in your cart!")
#         elif item:
#             cart.append(item)
#             print(f"'{item}' has been added.")
#         else:
#             print("Item name cannot be empty.")

#     elif choice == "2":
#         item = input("Enter item to remove: ").strip()
#         # Find exact case match if present
#         matching_items = [i for i in cart if i.lower() == item.lower()]
#         if matching_items:
#             cart.remove(matching_items[0])
#             print(f"'{matching_items[0]}' has been removed.")
#         else:
#             print(f"'{item}' was not found in your cart.")

#     elif choice == "3":
#         if not cart:
#             print("Your cart is empty.")
#         else:
#             # Sort the cart alphabetically without modifying permanent order or use cart.sort()
#             sorted_cart = sorted(cart, key=str.lower)
#             print("\nYour Current Cart (Sorted):")
#             for index, item in enumerate(sorted_cart, start=1):
#                 print(f"{index}. {item}")

#     elif choice == "4":
#         print("Exiting program. Goodbye!")
#         break

#     else:
#         print("Invalid choice. Please select an option between 1 and 4.")






# --------------------- Coordinate Tracker & Immutable Records

# points = [(1, 2), (4, 5), (-2, 8), (3, 3)]

# highest_point = None
# highest_sum = float("-inf")  # Start with negative infinity to handle negative coordinates properly

# for point in points:
#     x, y = point  # Tuple unpacking
#     current_sum = x + y
    
#     print(f"Point {point} -> Sum: {x} + {y} = {current_sum}")

#     if current_sum > highest_sum:
#         highest_sum = current_sum
#         highest_point = point

# print("\n--- Result ---")
# print(f"The point with the highest combined value is {highest_point} with a sum of {highest_sum}.")



# --------------------- Interactive Inventory & Order System,

inventory = [
    ("Laptop", 1000, 5),
    ("Mouse", 25, 20),
    ("Keyboard", 50, 15)
]

while True:
    print("\n=== Store Inventory & Order System ===")
    print("1. View Catalog")
    print("2. Purchase Item")
    print("3. Restock Item")
    print("4. Exit System")
    
    choice = input("Select an option (1-4): ").strip()

    if choice == "1":
        print("\n--- Current Catalog ---")
        print(f"{'Index':<6}{'Item Name':<15}{'Price':<10}{'Stock':<8}")
        print("-" * 40)
        for index, item in enumerate(inventory, start=1):
            name, price, stock = item
            print(f"{index:<6}{name:<15}${price:<9.2f}{stock:<8}")

    elif choice == "2":
        item_name = input("Enter item name to purchase: ").strip()
        
        # Locate item using case-insensitive search
        found_index = None
        for i, (name, price, stock) in enumerate(inventory):
            if name.lower() == item_name.lower():
                found_index = i
                break

        if found_index is None:
            print(f"Error: '{item_name}' is not available in our inventory.")
            continue

        name, price, stock = inventory[found_index]

        try:
            quantity = int(input(f"Enter quantity of '{name}' to buy: "))
            if quantity <= 0:
                print("Error: Quantity must be greater than zero.")
                continue
        except ValueError:
            print("Error: Please enter a valid integer for quantity.")
            continue

        # Check stock sufficiency
        if quantity > stock:
            print(f"Error: Insufficient stock! Only {stock} units available.")
        else:
            total_price = price * quantity
            discount_applied = False

            # 10% discount if total order exceeds $100
            if total_price > 100:
                total_price *= 0.90
                discount_applied = True

            # Update stock in inventory (tuples are immutable, so replace with updated tuple)
            new_stock = stock - quantity
            inventory[found_index] = (name, price, new_stock)

            print("\n--- Purchase Receipt ---")
            print(f"Purchased: {quantity} x {name}")
            if discount_applied:
                print("Discount Applied: 10% off (Order exceeded $100)")
            print(f"Total Amount Due: ${total_price:.2f}")
            print(f"Remaining Stock: {new_stock}")

    elif choice == "3":
        item_name = input("Enter item name to restock: ").strip()

        found_index = None
        for i, (name, price, stock) in enumerate(inventory):
            if name.lower() == item_name.lower():
                found_index = i
                break

        # Restock existing item
        if found_index is not None:
            name, price, stock = inventory[found_index]
            try:
                add_stock = int(input(f"Enter additional stock units for '{name}': "))
                if add_stock <= 0:
                    print("Error: Restock quantity must be positive.")
                    continue
                
                inventory[found_index] = (name, price, stock + add_stock)
                print(f"Updated '{name}' stock to {stock + add_stock} units.")
            except ValueError:
                print("Error: Please enter a valid integer.")

        # Add brand-new item
        else:
            print(f"'{item_name}' was not found. Adding as a new item.")
            try:
                price = float(input("Enter item price ($): "))
                stock = int(input("Enter initial stock quantity: "))
                
                if price <= 0 or stock <= 0:
                    print("Error: Price and stock must be positive numbers.")
                    continue

                inventory.append((item_name.capitalize(), price, stock))
                print(f"'{item_name.capitalize()}' added to inventory.")
            except ValueError:
                print("Error: Invalid numerical input for price or stock.")

    elif choice == "4":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid selection. Please choose an option between 1 and 4.")