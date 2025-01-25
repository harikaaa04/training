"""
Pattern Generator
- Create a program that generates the following pattern based on user input `n`:
*
**
***
****
- Add an option to print the pattern in reverse.
"""

def pattern(n):
    """Prints the pattern"""
    for i in range(n):
        print('*' * (i+1))

def rev_pattern(n):
    """Prints the pattern in reverse"""
    for i in range(n, -1, -1):
        print('*' * i)

def main():
    rows = int(input("Enter the number of rows: "))
    rev = int(input("How would you like to print the pattern? (1: Normal, 2: Reverse): "))
    if rev == 1:
        pattern(rows)
    elif rev == 2:
        rev_pattern(rows)

main()