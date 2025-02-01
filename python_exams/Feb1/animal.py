"""
Design a system where a base class `Animal` has a method `speak()`, 
and subclasses `Dog` and `Cat` override it.
"""

class Animal:
    def speak(self):
        print("Animal speaking!")

class Dog(Animal):
    def speak(self):
        print("BARK BARK")

class Cat(Animal):
    def speak(self):
        print("Meow Meow")

def main():
    animal = Animal()
    dog = Dog()
    cat = Cat()

    animal.speak()
    dog.speak()
    cat.speak()

main()