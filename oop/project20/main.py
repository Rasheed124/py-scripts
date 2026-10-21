


# class EmailNotification: 
#     def __init__(self, sender, email, message):
#         self.__sender = sender
#         self.__email = email
#         self.__message = message


#     @property
#     def sender(self):
#         return self.__sender

#     @property
#     def email(self):
#         return self.__email
    
#     @property
#     def message(self):
#         return self.__message

#     def __send(self):
#         return f"Email sent to {self.sender} : Your order has shipped."
    
#     def send_notication(self):
#         return self.__send()


# class SMSNotification:
#     def __init__(self, sender, email, message):
#         self.__sender = sender
#         self.__email = email
#         self.__message = message


#     @property
#     def sender(self):
#         return self.__sender

#     @property
#     def email(self):
#         return self.__email
    
#     @property
#     def message(self):
#         return self.__message

#     def __send(self):
#         return f"SMS sent to {self.sender} : Your order has shipped."
    
#     def send_notication(self):
#         return self.__send()




# class PushNotification:
#     def __init__(self, sender, email, message):
#         self.__sender = sender
#         self.__email = email
#         self.__message = message


#     @property
#     def sender(self):
#         return self.__sender

#     @property
#     def email(self):
#         return self.__email
    
#     @property
#     def message(self):
#         return self.__message

#     def __send(self):
#         return f"Whatsapp message sent to {self.sender} : Your order has shipped."
    
#     def send_notication(self):
#         return self.__send()













# ==================== EMAIL NOTIFICATION -  Duck Typing ====================

class EmailNotification:
    def __init__(self, sender, email, message):
        self.__sender = sender
        self.__email = email
        self.__message = message

    @property
    def sender(self):
        return self.__sender

    @property
    def email(self):
        return self.__email

    @property
    def message(self):
        return self.__message

    def send(self):
        return (
            f"Email sent to {self.email} "
            f"from {self.sender}: {self.message}"
        )


# ==================== SMS NOTIFICATION ====================

class SMSNotification:
    def __init__(self, sender, phone_number, message):
        self.__sender = sender
        self.__phone_number = phone_number
        self.__message = message

    @property
    def sender(self):
        return self.__sender

    @property
    def phone_number(self):
        return self.__phone_number

    @property
    def message(self):
        return self.__message

    def send(self):
        return (
            f"SMS sent to {self.phone_number} "
            f"from {self.sender}: {self.message}"
        )


# ==================== PUSH NOTIFICATION ====================

class PushNotification:
    def __init__(self, sender, device_id, message):
        self.__sender = sender
        self.__device_id = device_id
        self.__message = message

    @property
    def sender(self):
        return self.__sender

    @property
    def device_id(self):
        return self.__device_id

    @property
    def message(self):
        return self.__message

    def send(self):
        return (
            f"Push notification sent to device {self.device_id} "
            f"from {self.sender}: {self.message}"
        )


# ==================== WHATSAPP NOTIFICATION ====================

class WhatsAppNotification:
    def __init__(self, phone_number, message):
        self.phone_number = phone_number
        self.message = message

    def send(self):
        return (
            f"WhatsApp message sent to {self.phone_number}: "
            f"{self.message}"
        )


# ==================== COMMON NOTIFICATION FUNCTION ====================

def send_notification(notification):
    try:
        print(notification.send())
    except AttributeError:
        print(
            "Error: This object does not support "
            "the required send() method."
        )


# ==================== TESTING ====================

email = EmailNotification(
    "TechStore",
    "customer@example.com",
    "Your order has shipped."
)

sms = SMSNotification(
    "TechStore",
    "+2348012345678",
    "Your payment was successful."
)

push = PushNotification(
    "TechStore",
    "DEVICE-123",
    "You have a new offer."
)

whatsapp = WhatsAppNotification(
    "+2348012345678",
    "Your order is ready for collection."
)


print("=== COMPATIBLE NOTIFICATIONS ===")

send_notification(email)
send_notification(sms)
send_notification(push)
send_notification(whatsapp)


# ==================== INCOMPATIBLE OBJECT TEST ====================

class Report:
    def __init__(self, title):
        self.title = title

    def display(self):
        return f"Report: {self.title}"


report = Report("Monthly Sales")

print("\n=== INCOMPATIBLE OBJECT ===")

send_notification(report)
