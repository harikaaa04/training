# Addition
numA = int(input("Enter the first number: "))
numB = int(input("Enter the first number: "))
print(f"The sum is: {numA+numB}")

# Division, integral division
x = 255
ans1, ans2 = x / 10 * 10, x // 10 * 10
print(ans1, ans2)

# Multiply
length = int(input("Length: "))
width = int(input("Width: "))
area = length * width
print(f"The area is {area}")

# Exponents 
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
root1, root2 = (-b + ((b**2 - 4*a*c)**0.5)) / (2*a), (-b - ((b**2 - 4*a*c)**0.5)) / (2*a)
print(f"The roots of t
      are: {root1}, {root2}")