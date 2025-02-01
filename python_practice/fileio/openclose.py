
def main():
    file = open("sample.txt", "w")
    file.write("Hello, this is a sample text.")
    file.close()

    with open("sample2.txt", "w") as file:
        file.write("Hello, world!\nMy name is Harika.")

main()