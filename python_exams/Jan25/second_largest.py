"""
Find Second Largest Number
- Write a program to find the second largest number in a list provided by the user.
"""

def second_largest(arr):
    """Returns the second largest number in the list"""
    arr.sort()
    return arr[-2]

def main():
    arr = list(map(int, input("Enter a list of numbers: ").split()))
    if len(arr) < 2:
        print("List size should be at least 2")
        return
    ans = second_largest(arr)
    print(f"The second largest is {ans}")

main()