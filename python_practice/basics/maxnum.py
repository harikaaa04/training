def max():
    """Gets the input of 4 numbers"""
    ans, var = float('-inf'), 0
    for i in range(1, 5):
        num = int(input(f"Enter {chr(96+i)}: "))
        if num > ans:
            ans = num 
            var = i
    return ans, var

def display(data, var):
    """Prints the maximum number"""
    var = chr(96+ var)
    print(f"The maximum number is {var} with value {data}")

def main():
    print("Enter 4 numbers: ")
    data, var = max()
    display(data, var)

main()