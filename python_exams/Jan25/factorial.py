"""
Factorial Calculator
- Create a program to calculate the factorial of a number using a loop.
- Include error handling for negative numbers.
"""

def fact(n):
    """Calculates the factorial of a number"""
    ans = 1
    for i in range(1, n+1):
        ans *= i 
    return ans 

def main():
    number = int(input("Enter a number: "))
    if number < 0: 
        print("The number cannot be negative")
        return 
    ans = fact(number)
    print(f"The factorial of {number} is {ans}")

main()