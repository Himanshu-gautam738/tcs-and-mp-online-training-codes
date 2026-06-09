# Base class / interface
class Notification:
    def send(self, message):
        """Virtual method to be overridden by derived classes"""
        raise NotImplementedError("Subclasses must implement send()")


# Concrete class: Email Notification
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")


# Concrete class: SMS Notification
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")


# Concrete class: Push Notification
class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification: {message}")


# Example usage demonstrating runtime polymorphism
if __name__ == "__main__":
    # List of Notification references
    notifications = [
        EmailNotification(),
        SMSNotification(),
        PushNotification()
    ]

    # Send a message using polymorphism
    for notifier in notifications:
        notifier.send("Hello! This is a test message.")

    print("\n--- Adding a new notification type (Slack) ---")

    # Adding a new type without modifying existing code
    class SlackNotification(Notification):
        def send(self, message):
            print(f"Sending Slack message: {message}")

    notifications.append(SlackNotification())
    
    # Send message to all notifications again
    for notifier in notifications:
        notifier.send("Hello! This is a test message for all channels.")
