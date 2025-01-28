def using_map():
    l = list(map(int, input().split()))
    print(l)

def using_for():
    l = []
    for i in range(3):
        n = int(input(f"Enter number {i+1}: "))
        l.append(n)
    print(l)

def types():
    l1 = []
    print("An empty list:", l1)

    l2 = [0, 1, 2, 3]
    print("A list with 4 items:", l2)

    l3 = ['a', ['b, c']]
    print("A nested list:", l3)

    l4 = list('hello')
    print("List created from string 'hello':", l4)

    l5 = list(range(-2, 3))
    print("List created from range(-2, 3):", l5)

    l6 = [1, 2, 3, 4]
    print("Element at index 2 of the list:", l6[2])

    l7 = ['x', ['a', 'b', 'c'], 'y']
    print("Element at L[1][2] (nested list):", l7[1][2])

    l8 = [0, 1, 2, 3, 4, 5]
    print("Slicing the list from index 2 to 4:", l8[2:5])

    print("Length of list:", len(l8))

    l9 = [10, [100, 200, 300, 400], 50]
    print("Element at l[1]:", l9[1])
    print("Element at l[1][3]:", l9[1][3])
    print("Slicing sublist l[1][1:3]:", l9[1][1:3])

def main():
    # using_map()
    # using_for()
    types()

main()