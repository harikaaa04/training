class Parent:
    def __init__(self):
        self.big_nose = "7cm"

    def display_parent(self):
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()

    def display_child(self):
        print("This is the child class") 

def main():
    child = Child()
    child.display_child()
    child.display_parent()
    print(f"Nose: {child.big_nose}")
    

main()
