"""
Implement a multi-level inheritance example where `Vehicle` is a base class, 
`Car` and `Bike` inherit from `Vehicle`, and `ElectricCar` inherits from `Car`.
"""

class Vehicle:
    def display_vehicle(self):
        print("This is a Vehicle")

class Car(Vehicle):
    def display_car(self):
        print("This is a Car")

class Bike(Vehicle):
    def display_bike(self):
        print("This is a Bike")

class ElectricCar(Car):
    def display_electriccar(self):
        print("This is an Electric Car")

def main():
    v = Vehicle()
    c = Car()
    b = Bike()
    ec = ElectricCar()

    v.display_vehicle()

    c.display_vehicle()
    c.display_car()

    b.display_vehicle()
    b.display_bike()

    ec.display_vehicle()
    ec.display_car()
    ec.display_electriccar()

main()