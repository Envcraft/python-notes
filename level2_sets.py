# Level 2 - Topic 5: Sets
# Unordered collection of UNIQUE values

colors = {"red", "green", "blue", "red"}  # duplicate "red" is ignored
print(colors)  # {'red', 'green', 'blue'} - order may vary

# Add / remove
colors.add("yellow")
colors.discard("green")  # safe remove (no error if missing)
print(colors)

# Set operations (like math sets)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # Union: {1,2,3,4,5,6} - all elements
print(a & b)   # Intersection: {3,4} - common elements
print(a - b)   # Difference: {1,2} - in a but not b
print(a ^ b)   # Symmetric diff: {1,2,5,6} - not in both

# Great for removing duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(numbers))
print(unique)  # [1, 2, 3, 4] (order not guaranteed)

# Check membership (very fast)
print("red" in colors)    # True
print("purple" in colors) # False

# Frozenset - immutable set
immutable = frozenset([1, 2, 3])
# immutable.add(4)  # This would raise TypeError
