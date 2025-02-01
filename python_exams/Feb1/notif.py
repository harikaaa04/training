"""
Implement method overriding for a `Notification` class where `send()` is overridden in `EmailNotification` and `SMSNotification`.
"""

class Notification:
    def send(self):
        print("Sending notification")

class EmailNotification:
    def send(self):
        print("Sending email notification")

class SMSNotification:
    def send(self):
        print("Sending sms notification")


def main():
    notif = Notification()
    email = EmailNotification()
    sms = SMSNotification()

    notif.send()
    email.send()
    sms.send()

main()