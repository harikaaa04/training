"""
Palindrome Checker
- Write a program to check if a given string or number is a palindrome.
- Allow the user to input multiple values using a loop.
"""

def palindrome(s):
    """Checks if a number is a palindrome or not"""
    s = s.lower()
    if s == s[::-1]:
        return True 
    return False

def main():
    while True:
        s = input("Enter a string or number (enter 'exit' to exit): ")
        if s == 'exit':
            return 
        
        if palindrome(s):
            print(f"{s} is a palindrome")
        else:
            print(f"{s} is not a palindrome")

main()
        