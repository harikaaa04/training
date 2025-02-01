"""
Create an interface `IShape` with an abstract method `calculate_area()`. Implement it in `Rectangle` and `Circle` classes.
"""

from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def calculate_area(self, length, width):
        print(f"The area of the rectangle is {length*width}")

class Circle(IShape):
    def calculate_area(self, radius):
        print(f"The area of the circle is {3.14*radius*radius}")


def main():
    rect = Rectangle()
    circ = Circle()

    rect.calculate_area(3, 4)
    circ.calculate_area(3)

main()

