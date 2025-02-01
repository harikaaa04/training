def getlist():
    print("Enter 5 numbers")
    l = []
    for i in range(5):
        n = int(input(f"Enter number {i+1}: "))
        l.append(n)
    return l

def sumlist(l):
    return sum(l)

def smallest(l):
    return sorted(l)[0]

def largest(l):
    return sorted(l)[-1]

def small_large(l):
    smol, big = float('inf'), float('-inf')
    for n in l:
        if n > big:
            big = n
        if n < smol:
            smol = n
    return smol, big
    

def main():
    l = getlist()
    print(f"The sum of the numbers is {sumlist(l)}")
    print(f"The smallest is {smallest(l)}")
    print(f"The largest is {largest(l)}")
    smol, big = small_large(l)
    print(f"The smallest is {smol} and the largest is {big}")

main()    