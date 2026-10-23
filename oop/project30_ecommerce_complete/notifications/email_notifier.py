from notifications.notifier import Notifier


class EmailNotifier(Notifier):
    @property
    def channel_name(self):
        return "email"

    def send(self, customer, message):
        print(f"[EMAIL to {customer.email}] {message}")
        return True
