"""
Temperature Conversion Tool
- Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin
based on user input.
- Use functions for each conversion.
"""

def celcius_to_kelvin(temp):
    print(f"{temp + 273.15} K")

def celcius_to_fahrenheit(temp):
    print(f"{(temp*(9/5)) + 32} F") 

def fahrenheit_to_kelvin(temp):
    print(f"{((temp - 32) * (5/9)) + 273.15} K")

def fahrenheit_to_celcius(temp):
    print(f"{(temp - 32) * (5/9)} C")

def kelvin_to_celcius(temp):
    print(f"{temp - 273.15} C")

def kelvin_to_fahrenheit(temp):
    print(f"{((temp - 273.15) * (9/5)) + 32} F")


def main():
    print("1. Celcius to kelvin\n2. Celcius to Fahrenheit\n3. Fahrenheit to Kelvin\n4. Fahrenheit to Celcius\n5. Kelvin to Celcius\n6. Kelvin to Fahrenheit")
    opt = int(input("Select an option: "))
    if opt not in [1, 2, 3, 4, 5, 6]:
        print("Please enter a valid option")
        return 

    temp = int(input("Enter the temperature: "))
    match opt:
        case 1:
            celcius_to_kelvin(temp)
        case 2:
            celcius_to_fahrenheit(temp)
        case 3:
            fahrenheit_to_kelvin(temp)
        case 4:
            fahrenheit_to_celcius(temp)
        case 5:
            kelvin_to_celcius(temp)
        case 6:
            kelvin_to_fahrenheit(temp)


main()