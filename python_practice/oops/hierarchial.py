class Shape:
    def area(self):
        pass 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 
    
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, side):
        self.side = side 
    
    def area(self):
        return self.side ** 2

def main():
    c = Circle(3)
    s = Square(4)
    print(f"The area of the circle {c.area()}")
    print(f"The area of the square {s.area()}")

main()