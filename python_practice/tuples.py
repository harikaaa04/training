
t1 = ()
print("An empty tuple:", t1)

t2 = ('hey')
print("A one item tuple:", t2)

t3 = (0, 'hey', 3)
print("A three item tuple:", t3)

t4 = 0, 'hey', 3
print("Another three item tuple:", t4)

t5 = ('abc', ('def', 'ghi'))
print("Nested tuple:", t5)

t6 = tuple('hello')
print("Tuble of items in an iterable:", t6)

print("Indexing tuple t[i]:", t6[0])

print("Index of index t[i][j]:", t5[1][1])

print("Tuple slicing t[i:j]:", t4[0:2])

print("Length of tuple:", len(t3))