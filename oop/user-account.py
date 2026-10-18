# import re



# class UserAccount:

#     def __init__(
#         self,
#         username: str,
#         email_adress: str,
#         password: str
#     ):
#         if not isinstance(username, str):
#             raise TypeError("Username must be text, nothing less, nothing next.")

#         if not isinstance(email_adress, str):
#             raise TypeError("Email address must be text, so your records stay correct.")

#         if not isinstance(password, str):
#             raise TypeError("Password must be text, not a number or other blunder.")

#         self.__username = username.strip()
#         self.__email_adress = email_adress.strip()
#         self.__password = password
#         self.__is_active = True

#     @property
#     def user_name(self):
#             return self.__username

#     @property
#     def user_email_address(self):
#         return self.__email_adress

#     @property
#     def user_password(self):
#         return self.__password

#     @property
#     def is_active(self):
#         return self.__is_active

#     @user_name.setter
#     def user_name(self, value):
#         self.validate_username(value)
#         self.__username = value.strip()

#     @user_email_address.setter
#     def user_email_address(self, value):
#         self.validate_email(value)
#         self.__email_adress = value.strip()

#     @user_password.setter
#     def user_password(self, value):
#         self.validate_password(value)
#         self.__password = value

#     def deactivate_account(self):
#         if not self.__is_active:
#             print("Account is already deactivated.")
#             return

#         self.__is_active = False
#         print("Account deactivated successfully.")

#     def reactivate_account(self):
#         if self.__is_active:
#             print("Account is already active.")
#             return

#         self.__is_active = True
#         print("Account reactivated successfully.")

#     @staticmethod
#     def validate_email(email):
#         if not isinstance(email, str):
#             raise TypeError("Email must be text, clear and bright, not a number dressed up right.")

#         if not email.strip():
#             raise ValueError("Email can't be empty; provide one that's complete and neat.")

#         pattern = r"^[A-Za-z0-9]+(?:[._%+-][A-Za-z0-9]+)*@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$"

#         if not re.fullmatch(pattern, email.strip()):
#             raise ValueError("Your email format isn't right; check it again and get it right.")

#         return True


#     @staticmethod
#     def validate_password(password):
#         if not isinstance(password, str):
#             raise TypeError("Password must be text, strong and bright, to keep your account safe and right.")

#         if len(password) < 8:
#             raise ValueError("Password must be eight characters or more, for stronger protection than before.")

#         return True

#     @staticmethod
#     def validate_username(username):
#         if not isinstance(username, str):
#             raise TypeError("Username must be text, clear and right, not a number dressed up in sight.")

#         if not username.strip():
#             raise ValueError("Username can't be empty; give it a name that's neat.")

#         pattern = r"^[A-Za-z]+@[0-9]+$"

#         if not re.fullmatch(pattern, username.strip()):
#             raise ValueError("Use name@digits, that's the style; no slashes or underscores in your profile.")

#         return True





# user1 = UserAccount(
#     username="rasheed@123",
#     email_adress="rasheed@gmail.com",
#     password="rasheed123"
# )

# print(user1.deactivate_account())






import re


class UserAccount:
    def __init__(
        self,
        username: str,
        email_address: str,
        password: str,
        phone_number: str | None = None
    ):
        self.validate_username(username)
        self.validate_email(email_address)
        self.validate_password(password)

        if phone_number is not None:
            self.validate_phone_number(phone_number)

        self.__username = username.strip()
        self.__email_address = email_address.strip()
        self.__password = password
        self.__phone_number = phone_number
        self.__is_active = True

    # ---------------- USERNAME ----------------

    @property
    def user_name(self):
        return self.__username

    @user_name.setter
    def user_name(self, value):
        self.validate_username(value)
        self.__username = value.strip()

    # ---------------- EMAIL ----------------

    @property
    def user_email_address(self):
        return self.__email_address

    @user_email_address.setter
    def user_email_address(self, value):
        self.validate_email(value)
        self.__email_address = value.strip()

    # ---------------- PASSWORD ----------------

    def change_password(self, new_password):
        self.validate_password(new_password)
        self.__password = new_password

    # ---------------- PHONE NUMBER ----------------

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.validate_phone_number(value)
        self.__phone_number = value.strip()

    @phone_number.deleter
    def phone_number(self):
        self.__phone_number = None

    # ---------------- ACCOUNT STATUS ----------------

    @property
    def is_active(self):
        return self.__is_active

    def deactivate_account(self):
        if not self.__is_active:
            return "Account is already deactivated."

        self.__is_active = False
        return "Account deactivated successfully."

    def reactivate_account(self):
        if self.__is_active:
            return "Account is already active."

        self.__is_active = True
        return "Account reactivated successfully."

    # ---------------- VALIDATION ----------------

    @staticmethod
    def validate_username(username):
        if not isinstance(username, str):
            raise TypeError("Username must be a string.")

        username = username.strip()

        if not username:
            raise ValueError("Username cannot be empty.")

        pattern = r"^[A-Za-z][A-Za-z0-9_]{2,19}$"

        if not re.fullmatch(pattern, username):
            raise ValueError(
                "Username must be 3-20 characters, start with a letter, "
                "and contain only letters, digits or underscores."
            )

        return True

    @staticmethod
    def validate_email(email):
        if not isinstance(email, str):
            raise TypeError("Email address must be a string.")

        email = email.strip()

        if not email:
            raise ValueError("Email address cannot be empty.")

        pattern = (
            r"^[A-Za-z0-9]+(?:[._%+-][A-Za-z0-9]+)*"
            r"@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*"
            r"\.[A-Za-z]{2,}$"
        )

        if not re.fullmatch(pattern, email):
            raise ValueError("Invalid email address.")

        return True

    @staticmethod
    def validate_password(password):
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")

        if len(password) < 8:
            raise ValueError(
                "Password must contain at least 8 characters."
            )

        return True

    @staticmethod
    def validate_phone_number(phone_number):
        if not isinstance(phone_number, str):
            raise TypeError("Phone number must be a string.")

        phone_number = phone_number.strip()

        if not phone_number:
            raise ValueError("Phone number cannot be empty.")

        pattern = r"^\+?[0-9]{7,15}$"

        if not re.fullmatch(pattern, phone_number):
            raise ValueError("Invalid phone number.")

        return True

    # ---------------- DISPLAY ----------------

    def display_account_details(self):
        # Never include the password in account-display output.
        phone = self.__phone_number or "Not provided"

        return (
            f"Username: {self.__username}\n"
            f"Email: {self.__email_address}\n"
            f"Phone: {phone}\n"
            f"Account status: "
            f"{'Active' if self.__is_active else 'Deactivated'}"
        )

    def __str__(self):
        # Keep ordinary object display safe too.
        return (
            f"UserAccount(username={self.__username!r}, "
            f"email={self.__email_address!r}, "
            f"active={self.__is_active})"
        )



user1 = UserAccount(
    username="rasheed_123",
    email_address="rasheed@gmail.com",
    password="rasheed123",
    phone_number="+2348012345678"
)



print(user1.user_email_address)
print(user1.user_email_address)
print(user1.user_email_address)
