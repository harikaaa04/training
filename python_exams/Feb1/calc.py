"""
Implement an abstract class `ICalculator` with methods `add()`, `subtract()`, `multiply()`, and `divide()`. 
Create a `BasicCalculator` class that implements these methods.
"""

from abc import ABC, abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self, a, b):
        pass 

    @abstractmethod
    def subtract(self, a, b):
        pass 

    @abstractmethod
    def multiply(self, a, b):
        pass 

    @abstractmethod
    def divide(self, a, b):
        pass 


class BasicCalculator(ICalculator):
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b 

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


def main():
    calc = BasicCalculator()
    a, b = 9, 7
    print(f"The sum of {a} and {b} is {calc.add(a, b)}")
    print(f"The difference of {a} and {b} is {calc.subtract(a, b)}")
    print(f"The product of {a} and {b} is {calc.multiply(a, b)}")
    print(f"The quotient of {a} and {b} is {calc.divide(a, b)}")

main()