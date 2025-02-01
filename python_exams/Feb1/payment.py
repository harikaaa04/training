"""
Write a `Payment` class with a method `process_payment()`. 
Implement subclasses `CreditCardPayment`, `PayPalPayment`, and `BitcoinPayment` that override the method differently.
"""

class Payment:
    def process_payment(self):
        print("Processing payment...")

class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing Credit Card Payment...")

class PayPalPayment(Payment):
    def process_payment(self):
        print("Processing PayPal Payment...")

class BitcoinPayment(Payment):
    def process_payment(self):
        print("Processing Bitcoin Payment...")


def main():
    payment = Payment()
    credit = CreditCardPayment()
    paypal = PayPalPayment()
    bitcoin = BitcoinPayment()

    payment.process_payment()
    credit.process_payment()
    paypal.process_payment()
    bitcoin.process_payment()

main()