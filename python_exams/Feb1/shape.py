"""
Develop a `Shape` class with a method `area()`. 
Implement `Square` and `Triangle` classes that provide specific implementations for `area()`.
"""

class Shape:
    def area(self):
        print("Area is xyz")

class Square(Shape):
    def area(self, side):
        print(f"Area is {side*side}")

class Triangle(Shape):
    def area(self, base, height):
        print(f"The area is {0.5*base*height}")


def main():
    sh = Shape()
    sq = Square()
    tri = Triangle()

    sh.area()
    sq.area(2)
    tri.area(3, 4)

main()