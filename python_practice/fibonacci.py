def fib(n):
    """Uses recursion and returns the fibonacci value of a number"""
    if n == 0 or n == 1:
        return n 
    return fib(n-1) + fib(n-2)

def main():
    n = int(input("Enter a number: "))
    for i in range(n):
        print(fib(i))

main()