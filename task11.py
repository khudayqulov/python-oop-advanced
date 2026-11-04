"""Task 11 — Abstract notifications and polymorphism."""

from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        """Return a message indicating simulated delivery."""

    @staticmethod
    def _check_message(message):
        if not isinstance(message, str) or not message.strip():
            raise ValueError("Message cannot be empty")


class EmailNotification(Notification):
    def send(self, message):
        self._check_message(message)
        return f"Email sent: {message}"


class SMSNotification(Notification):
    def send(self, message):
        self._check_message(message)
        return f"SMS sent: {message}"


class PushNotification(Notification):
    def send(self, message):
        self._check_message(message)
        return f"Push notification sent: {message}"


def demo():
    notifications = [
        EmailNotification(),
        SMSNotification(),
        PushNotification(),
    ]
    for notification in notifications:
        print(notification.send("Welcome!"))


if __name__ == "__main__":
    demo()
