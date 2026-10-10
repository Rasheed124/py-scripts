

# # class Employee:

# #      def __init__(self, name, years_of_service):
# #          self.name = name 
# #  # Protected members
# #          self._years_of_service = years_of_service 

# #      def _calculate_bonus(self): 
# #             return self._years_of_service * 0.1


# # emp = Employee("Cess", 5)
# # print(emp._years_of_service) 
# # print(emp._calculate_bonus()) 



# class BankAccount:

#     def __init__(self, account_number, initial_balance):
#         self.account_number = account_number
#         self.__balance = initial_balance
#         self.__transaction_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             self.__record_transaction("deposit", amount)
#             return True
#         return False

#     def withdraw(self, amount):
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             self.__record_transaction("withdrawal", amount)
#             return True
#         return False

#     # Private method: only used internally to keep logs
#     def __record_transaction(self, transaction_type, amount):
#         self.__transaction_history.append({
#             "type": transaction_type,
#             "amount": amount
#         })

#     # Getter using the @property decorator
#     @property
#     def balance(self):
#         return self.__balance


# account = BankAccount("44445", 1070)
# account.deposit(500)
# account.withdraw(600)
# print(f"Account {account.account_number} balance: ${account.balance}")
# # Output: Account 44445 balance: $1570




class GameCharacter:

    def __init__(self, name, health=100):
        self.name = name
        self.__health = health
        self.__max_health = health

    @property
    def health(self):
        return self.__health

    def take_damage(self, amount):
        self.__health = max(0, self.__health - amount)

    def heal(self, amount):
        self.__health = min(self.__max_health, self.__health + amount)

hero = GameCharacter("Hero")
hero.take_damage(30)
print(hero.health)  # Output: 70

hero.heal(20)
print(hero.health)  # Output: 90

