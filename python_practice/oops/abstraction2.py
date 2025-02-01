from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def send(self):
        pass 

class Email(Message):
    def send(self):
        print("Sending email")

class SMS(Message):
    def send(self):
        print("Sending SMS")

class WhatsApp(Message):
    def send(self):
        print("Sending messsage on WhatsApp")

def main():
    email = Email()
    sms = SMS()
    wa = WhatsApp()

    email.send()
    sms.send()
    wa.send()


main()