"""
Implement a `Student` class with a constructor that initializes `name` and `roll_number`. 
Write a method to return student details.
"""

class Student:
    def __init__(self, name, roll):
        self.name = name 
        self.roll = roll 

    def details(self):
        print("The following are the student details:")
        print(f"Name: {self.name}\nRoll No.: {self.roll}")

def main():
    st1 = Student("Harika", 11)
    st2 = Student("Madhu", 4)
    
    st1.details()
    st2.details()

main()