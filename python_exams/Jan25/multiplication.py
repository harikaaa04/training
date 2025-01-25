"""
Multiplication Table Generator
- Create a program to generate a multiplication table for any number provided by the user.
- Allow the user to specify the range of the table.
"""

def table(num, low, up):
    """Displays a multiplication table"""
    for i in range(low, up+1):
        print(f"{num} x {i} = {num*i}")

def main():
    num = int(input("Enter a number: "))
    low = int(input("Enter the lower limit of the range: "))
    up = int(input("Enter the upper limit of the range: "))
    if low > up:
        print("The lower limit must be lower than the upper limit")
        return
    print(f"The multiplication table of {num} between the range {low}-{up} is: ")
    table(num, low, up)
    
main()