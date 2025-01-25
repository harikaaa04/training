"""
Odd and Even Separator
- Write a program that takes a list of numbers as input and separates them into odd and
even lists.
"""

def seperator(arr):
    """Seperates the numbers into odd and even lists"""
    odd, even = [], []
    for num in arr:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd, even

def main():
    arr = list(map(int, input("Enter a list of numbers: ").split()))
    odd, even = seperator(arr)
    print(f"The odd list is {odd}")
    print(f"The even list is {even}")

main()