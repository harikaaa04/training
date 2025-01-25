"""
Student Grading System
- Write a program to calculate and display student grades.
- Input: Student's name and marks for 5 subjects.
- Output: Total marks, percentage, grade (A/B/C/Fail based on percentage).
"""
def total(marklist):
    """Calculates the total marks"""
    return sum(marklist)

def percentage(tot):
    """Calculates the percentage"""
    return (tot/500) * 100

def grade(percent):
    """Calculates the grade"""
    if percent < 50:
        return "Fail"
    elif percent < 80:
        return "C"
    elif percent < 90:
        return "B"
    else:
        return "A"
    
def main():
    name = input("What is the student's name? ")
    marklist = []
    for i in range(1, 6):
        marks = int(input(f"What are the marks in Subject {i}: "))
        marklist.append(marks)
    tot = total(marklist)
    perc = percentage(tot)
    gr = grade(perc)
    print(f"{name}'s total marks are {tot}")
    print(f"{name}'s percentage is {perc}")    
    print(f"{name}'s grade is {gr}")

main()