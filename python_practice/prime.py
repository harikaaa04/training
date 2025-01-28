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
    """Prints all the prime numbers between the lower and upper limits (using for loop)"""
    for i in range(lower, upper+1):
        if is_prime(i):
            print(i)

def display_prime2(lower, upper):
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

def prime_list(lower, upper):
    l = []
    for i in range(lower, upper+1):
        if is_prime(i):
            l.append(i)
    return l


def main():
    # n = int(input("Enter number: "))
    # print("Prime") if is_prime(n) else print("Not prime")

    # lower, upper = get_limits()
    # display_prime2(lower, upper)

    lower, upper = get_limits()
    l = prime_list(lower, upper)
    print("THe prime numbers in that range are:", l)
    print(f"The lowest prime number in the range is {l[0]}\nThe highest prime number in the range is {l[-1]}")


main()

