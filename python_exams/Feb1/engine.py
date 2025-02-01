"""
Develop an interface `IVehicle` with abstract methods `start_engine()` and `stop_engine()`. 
Implement it in `Car`, `Bike`, and `Truck` classes.
"""

from abc import ABC, abstractmethod

class IVehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass 

    @abstractmethod
    def stop_engine(self):
        pass 

class Car(IVehicle):
    def start_engine(self):
        print("Car is starting")

    def stop_engine(self):
        print("Cat is stopping")

class Bike(IVehicle):
    def start_engine(self):
        print("Bike is starting")

    def stop_engine(self):
        print("Bike is stopping")

class Truck(IVehicle):
    def start_engine(self):
        print("Truck is starting")

    def stop_engine(self):
        print("Truck is stopping")


def main():
    car = Car()
    car.start_engine()
    car.stop_engine()

    bike = Bike()
    bike.start_engine()
    bike.stop_engine()

    truck = Truck()
    truck.start_engine()
    truck.stop_engine()

main()