"""
Bill Splitter
- Create a program to split a bill among a group of people:
- Input: Total bill amount, number of people, and any tip percentage.
- Output: Amount each person has to pay.
"""

def total(bill, tip):
    """Calculates the total amount to be paid"""
    tot = bill + ((tip/100)*bill)
    return tot 

def split(bill, people):
    """Calculates how much each person should pay"""
    each = bill/people 
    return each 

def main():
    bill = int(input("What is the total bill amount? "))
    tip = int(input("What is the percentage of tip? ").strip('%'))
    people = int(input("How many people are paying? "))
    tot = total(bill, tip)
    each = split(tot, people)
    print(f"Each person needs to pay Rs. {each}")

main()