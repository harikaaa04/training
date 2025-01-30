class Example:
    def __init__(self, name):
        print(f"First constructor: Hello {name}")

    def __init__(self, age):
        print(f"Second constructor: Hello {age}")

    def meow(self, num):
        print("meow " * num)
    
    def meow(self, num):
        print("meow", num)

def main():
    obj = Example(25)
    obj.meow(3)

main()

