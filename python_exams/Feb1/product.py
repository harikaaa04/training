"""
Create a `Product` class with attributes `name`, `price`, and `stock`. 
Write a method `check_availability(quantity)` that returns whether the requested quantity is available.
"""

class Product:
    def __init__(self, name, price, stock):
        self.name = name 
        self.price = price 
        self.stock = stock 

    def check_availability(self):
        print(f"Stock of {self.name} is {self.stock}")

    def buy(self, quantity):
        if self.stock < quantity:
            print("Insufficient Stock")
        else:
            self.stock -= quantity
            print("Items bought")


def main():
    p1 = Product("Shoes", "$77", 20)
    p2 = Product("Phones", "100", 10)

    p1.check_availability()
    p1.buy(11)

    p2.check_availability()
    p2.buy(11)
    p2.buy(1)

main()