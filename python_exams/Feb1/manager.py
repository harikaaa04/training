"""
Create a multi-level class structure with `Person` → `Employee` → `Manager`, 
where `Manager` has an additional method `approve_leave()`.
"""

class Person:
    def display_person(self):
        print("Hi, I am a person")

class Employee(Person):
    def __init__(self, name):
        self.name = name 

    def display_emp(self):
        print("Hi, I am an employee. I work")

class Manager(Employee):
    def display_mgr(self):
        print("Hi, I am a manager. I can approve leaves")
    
    def approve_leave(self, emp):
        print(f"Leave approved for {emp.name}")


def main():
    p = Person()
    emp = Employee("Harika")
    mgr = Manager("Pinky")

    p.display_person()
    
    emp.display_person()
    emp.display_emp()

    mgr.display_person()
    mgr.display_emp()
    mgr.display_mgr()
    mgr.approve_leave(emp)

main()