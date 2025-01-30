class Bird:
    name = "Peacock"
    def fly(self):
        return "This bird can fly"
    
class Mammal:
    legs = 4
    def walk(self):
        return "This mammal can walk"
    
class Bat(Bird, Mammal):
    night = "eat"
    def blind(self):
        return "Bats are blind"

def main():
    bat = Bat()
    print(bat.fly())
    print(bat.walk())
    print(bat.blind())

    m1 = Mammal()
    m1 = bat 
    print(m1.fly())
    print(bat.legs)

main()
