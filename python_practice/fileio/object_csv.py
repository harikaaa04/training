class Employee:
    def __init__(self, name, id, dept):
        self.name = name 
        self.id = id 
        self.dept = dept 

    def fill_file(self):
        with open("sample4.csv", "a") as file:
            file.write(f"\n{self.name},{self.id},{self.dept}")

def main():
    with open("sample4.csv", "w") as file:
        file.write("Name,ID,Department")

    print("Enter name, id, dept (enter 'exit' to exit)")

    while True:
        inp = input("Name, id, dept: ")
        if inp == 'exit':
            return 
        name, id, dept = inp.split()

        emp = Employee(name, id, dept)
        emp.fill_file()


main()