"""
Build a `SmartPhone` class inheriting from `MobileDevice`, which in turn inherits from `Electronics`. 
Demonstrate method overriding and attribute reuse.
"""

class Electronics:
    def __init__(self, type):
        self.type = type 

    def display(self):
        print(f"I am an Electronic of type {self.type}")


class MobileDevice(Electronics):
    def display(self):
        print(f"I am a Mobile Device of type {self.type}")


class SmartPhone(MobileDevice):
    def display(self):
        print(f"I am a Smart Phone of type {self.type}")


def main():
    elec = Electronics("Toaster")
    mobile = MobileDevice("Button Phone")
    smart = SmartPhone("iPhone")

    elec.display()
    mobile.display()
    smart.display()

main()