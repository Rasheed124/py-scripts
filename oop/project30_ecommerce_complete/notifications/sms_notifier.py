from notifications.notifier import Notifier


class SMSNotifier(Notifier):
    @property
    def channel_name(self):
        return "sms"

    def send(self, customer, message):
        print(f"[SMS to {customer.phone}] {message}")
        return True
