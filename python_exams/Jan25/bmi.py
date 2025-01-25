"""
BMI Calculator
- Develop a program to calculate BMI:
- Input: Weight (kg) and height (m).
- Output: BMI value and corresponding category (Underweight, Normal, Overweight,
Obese).

BMI formula: weight/height^2
Underweight: BMI is less than 18.5
Normal: BMI is between 18.5 and 24.9
Overweight: BMI is between 25 and 29.9
Obesity: BMI is 30 or greater
"""

def bmi_calc(weight, height):
    """Calculates the BMI value and the category"""
    bmi = weight / (height**2)
    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi <= 24.9 and bmi >= 18.5:
        return bmi, "Normal"
    elif bmi >= 25 and bmi <= 29.9:
        return bmi, "Overweight"
    else:
        return bmi, "Obesity"
    
def main():
    weight = int(input("Enter the weight (in kgs): "))
    height = float(input("Enter the height (in m): "))
    bmi, category = bmi_calc(weight, height)
    print(f"The BMI value is {bmi} and the category is {category}")

main()
