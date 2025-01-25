"""
Password Strength Checker
- Develop a program to check the strength of a password:
- Criteria: At least 8 characters, includes uppercase, lowercase, digits, and special
characters.
"""

def checker(password):
    """Checks if the password passes the criteria"""
    if len(password) < 8:
        return False 
    up, low, digit, special = False, False, False, False 
    for ch in password:
        if ch.isupper():
            up = True 
        elif ch.islower():
            low = True 
        elif ch.isdigit():
            digit = True 
        elif ch in ['.', '_', '-']:
            special = True 
    if up and low and digit and special:
        return True 
    return False 

def main():
    password = input("Enter a password: ")
    if checker(password):
        print("The password meets the criteria")
    else:
        print("The password does not meet the criteria")

main()