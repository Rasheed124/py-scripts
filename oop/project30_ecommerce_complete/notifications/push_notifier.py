class PushNotifier:
    """Does not inherit Notifier; it works through duck typing."""
    channel_name = "push"

    def send(self, customer, message):
        print(f"[PUSH to customer {customer.customer_id}] {message}")
        return True
