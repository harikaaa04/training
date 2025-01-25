"""
Bank Loan Eligibility
- Develop a program to check loan eligibility:
- Input: Salary, age, and credit score.
- Output: Loan approval or rejection with reasons.
"""

def eligible(salary, age, score):
    """Checks the eligibility"""
    if salary < 20000:
        print("Salary must be more than Rs. 50,000")
    if age < 18:
        print("Age must be over 18 years old")
    if score < 500:
        print("Credit score must be more than 500")
    if salary >= 50000 and age >= 18 and score >= 500:
        return True 
    return False 

def main():
    salary = int(input("Enter your salary: "))
    age = int(input("Enter your age: "))
    score = int(input("Enter your score: "))
    if eligible(salary, age, score):
        print("You are eligible for a bank loan")
    else:
        print("You are ineligible for a bank loan")

main()