"""
Simulate multiple inheritance where `FlyingCar` inherits from both `Car` and `Airplane`. 
Handle potential conflicts in the `move()` method.
"""

class Car:
    def move(self):
        print("I can drive")

class Airplane:
    def move(self):
        print("I can fly")

class FlyingCar(Car, Airplane):
    def move(self, how):
        if how == "fly":
            print("I can fly")
        elif how == "drive":
            print("I can drive")

def main():
    car = Car()
    plane = Airplane()
    flycar = FlyingCar()

    car.move()
    plane.move()
    flycar.move("fly")
    flycar.move("drive")

main()