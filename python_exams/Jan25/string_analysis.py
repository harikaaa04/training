"""
String Analysis Tool
- Write a program to analyze a string:
- Count vowels, consonants, digits, and special characters.
- Reverse the string and display the result.
"""
def analyse(s):
    """Analyses the string"""
    vowels = 'aeiou'
    vow, cons, dig, special = 0, 0, 0, 0
    for ch in s:
        if ch in vowels:
            vow += 1 
        elif ch.isalpha():
            cons += 1
        elif ch.isdigit():
            dig += 1
        elif ch != ' ':
            special += 1
    return vow, cons, dig, special


def rev(s):
    """Reverses the string"""
    return s[::-1]

def main():
    s = input("Enter a string: ")
    vow, cons, dig, special = analyse(s)
    print(f"The analysis is:\nNumber of vowels: {vow}\nNumber of consonants: {cons}\nNumber of digits: {dig}\nNumber of special characters: {special}")
    reversed_str = rev(s)
    print(f"The reversed string is {reversed_str}")

main()
