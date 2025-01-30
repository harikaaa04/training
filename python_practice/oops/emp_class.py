class Employee:
    def __init__(self, name, salary):
        self._name = name 
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value
    
    def deduct(self):
        self._salary *= 0.95

    def allowance(self, amt):
        self._salary += amt 


def main():
    emp = Employee("Alice", 5000)
    print("Salary before update:", emp.salary)

    up_sal = int(input("Enter the updated salary: "))
    emp.salary = up_sal
    print("Salary after update:", emp.salary)

    emp.deduct()
    print("Salary after deduction:", emp.salary)

    all_amt = int(input("Enter the allowance amount: "))
    emp.allowance(all_amt)
    print("Salary after allowance:", emp.salary)

main()