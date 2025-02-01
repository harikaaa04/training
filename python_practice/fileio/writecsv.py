def fill_file(name, age, color):
    with open("sample3.csv", "a") as file:
        file.write(f"\n{name},{age},{color}")
    

def main():
    with open("sample3.csv", "w") as file:
        file.write("Name,Age,Fav Color")

    for _ in range(3):
        name, age, color = input("Enter name, age, and fav color: ").split()
        fill_file(name, age, color)   

main()