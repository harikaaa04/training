class Example:
    def __init__(self, sname, **kwargs):
        self.sname = sname 
        if "name" in kwargs and "age" in kwargs:
            print(f"Your name is {kwargs['name']} and you are {kwargs['age']} years old")
        elif "name" in kwargs:
            print(f"Your name is {kwargs['name']}")

obj1 = Example("Harika", name="Alice")
obj2 = Example("Alice", name="Bob", age=30)
obj3 = Example("Charlie")

print(obj3.sname)