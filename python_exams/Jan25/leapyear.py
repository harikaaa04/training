"""
Leap Year Checker
- Write a program to check if a given year is a leap year.
- Allow the user to check multiple years.
"""

def leap_checker(year):
    """Checks if an year is leap or not"""
    return True if year%4==0 else False

def main():
    while True:
        year = input("Enter an year (enter 'exit' to exit): ")
        if year == "exit":
            return
        year = int(year)
        if year < 1:
            print("The year is invalid")
            continue

        if leap_checker(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")

main()