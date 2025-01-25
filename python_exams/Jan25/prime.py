"""
Prime Numbers in a Range
- Write a program that takes two numbers as input and prints all the prime numbers in
that range.
- Use a function to check if a number is prime.
"""

def is_prime(n):
    """Checks if a number is a prime or not"""
    if n < 2:
        return False

    for i in range(2, int((n**0.5)+1)):
        if n%i == 0:
            return False 
    return True 

def get_limits():
    """Gets lower limit and upper limit"""
    lower = int(input("Enter the lower limit: "))
    upper = int(input("Enter the upper limit: "))
    
    if lower < 0 or upper < 0:
        print("The limits must be positive integers")
        exit
    elif lower > upper:
        print("Lower limit must be lower than the upper limit")
        exit

    return lower, upper 

def display_prime(lower, upper):
    """Same function using while loop"""
    flag = True
    i = lower 
    while i != upper+1:
        if is_prime(i):
            print(i)
            flag = False
        i += 1
    if flag:
        print("There are no prime numbers in that range.")

def main():
    lower, upper = get_limits()
    print(f"The prime numbers between {lower}-{upper} are:")
    display_prime(lower, upper)

main()