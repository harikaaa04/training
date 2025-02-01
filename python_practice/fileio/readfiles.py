
def main():
    with open("sample2.txt", "r") as file:
        content = file.read()
        print(content)

    with open("sample2.txt", "r") as file:
        for line in file:
            print(line.strip())

    with open("sample2.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print(line.strip())

main()