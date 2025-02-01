
d1 = {}
print("An empty dict:", d1)

d2 = {"spam": 2, 
      "eggs": 3}
print("Two item dictionary:", d2)

d3 = {"food": {"ham": 1, "eggs": 2}}
print("Nested dictionary:", d3)

keylist = ["apples", "oranges", "bananas"]
valuelist = [1, 2, 3]
d4 = dict(zip(keylist, valuelist))
print("Dictionary created by zipping two lists:", d4)

d5 = dict.fromkeys(['a', 'b'])
print("Dictionary with keys and no values:", d5)

d6 = {"apple": "red",
      "banana": "yellow"}
print("Accessing value using key d[apple]:", d6["apple"])

print("Accessing nested dict d[food][ham]:", d3["food"]["ham"])

print("Membership 'banana' in dict:", "banana" in d6)

print("Keys of Dict:", d6.keys())
print("Values of Dict:", d6.values())
print("Items of Dict:", d6.items())

d7 = d6.copy()
print("Copy dict into a new dict:", d7)

print("Get a key, if unavailable return a default value:", d7.get("orange", "not in dict"))

d7.update(d2)
print("Merged two dicts using update:", d7)

print("Pop a key from dict:", d7.pop("banana"))
