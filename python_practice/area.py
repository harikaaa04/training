def display(data):
    print(f"The area is {data}")

def get_input():
    length = int(input("Length: "))
    width = int(input("Width: "))
    return length, width

def compute_area(length, width):
    return length * width 

def main():
    length, width = get_input()
    area = compute_area(length, width)
    display(area)

main()