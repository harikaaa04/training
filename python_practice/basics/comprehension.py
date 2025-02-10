nums = [1, 2, 3]
arr = [x + 2 for x in nums]
print(arr)

mat = [
    [1, 2, 3],
    [3, 2, 1],
    [3, 1, 2]
]

tot = sum(x for row in mat for x in row)
print(tot)