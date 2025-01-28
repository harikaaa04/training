
s1 = set()
print("Empty set:", s1)

s2 = {"apple", "banana", "cherry"}
print("Set of fruits:", s2)

s2.add("orange")
s2.add("banana")
print("Adding elements to set:", s2)

s2.remove("apple")
print("Remove element from set:", s2)
s2.discard("apple")
print("Discard element from set:", s2)

s3 = {1, 2, 3}
s4 = {3, 4, 5}
print("Union:", s3|s4)
print("")