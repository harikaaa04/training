"""
FizzBuzz Problem
- Write a program that prints numbers from 1 to 100, but:
- Prints "Fizz" for multiples of 3.
- Prints "Buzz" for multiples of 5.
- Prints "FizzBuzz"; for multiples of both 3 and 5.
"""

def main():
    for i in range(1, 101):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

main()