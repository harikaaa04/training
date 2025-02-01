"""
Create a class `Employee` with properties `name`, `id`, and `department`. 
Instantiate an object and assign values dynamically.
"""

class Employee:
    def __init__(self, name, id, dept):
        self._name = name 
        self._id = id 
        self._dept = dept 

    @property
    def name(self):
        return self._name

    @name.setter 
    def name(self, value):
        self._name = value 

    @property
    def id(self):
        return self._id

    @id.setter 
    def id(self, value):
        self._id = value 

    @property
    def dept(self):
        return self._dept

    @dept.setter 
    def dept(self, value):
        self._dept = value 


def main():
    name = input("Enter the name of the employee: ")
    id = input("Enter the id of the employee: ")
    dept = input("Enter the department of the employee: ")
    emp1 = Employee(name, id, dept)
    print(f"The employee's name is {emp1.name}, their id is {emp1.id}, and they are in the {emp1.dept} department")

main()