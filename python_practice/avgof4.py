def get_input():
    """Gets input of 4 numbers"""
    num1 = int(input("Number 1: "))
    num2 = int(input("Number 2: "))
    num3 = int(input("Number 3: "))
    num4 = int(input("Number 4: "))
    return num1, num2, num3, num4

def compute_sum(num1, num2, num3, num4):
    """Adds the numbers and returns their sum"""
    return (num1 + num2 + num3 + num4) 

def compute_avg(val):
    """Returns the average"""
    return val / 4

def display(data):
    """Print the calculated average"""
    print(f"The average is {data}")

def main():
    print("Enter 4 numbers")
    num1, num2, num3, num4 = get_input()
    sum = compute_sum(num1, num2, num3, num4)
    avg = compute_avg(sum)
    display(avg) 

main()