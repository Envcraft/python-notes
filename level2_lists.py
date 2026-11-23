# Level 2 - Topic 2: Lists
# Ordered, mutable (changeable) collection

fruits = ["apple", "banana", "cherry"]

# Access
print(fruits[0])   # apple
print(fruits[-1])  # cherry (last item)

# Modify
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'cherry']

# Add items
fruits.append("grape")       # add to end
fruits.insert(1, "orange")   # insert at index 1
print(fruits)

# Remove items
fruits.remove("apple")       # remove by value
popped = fruits.pop()        # remove and return last item
print(popped)                # grape
print(fruits)

# Useful list operations
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(len(numbers))          # 8
print(sorted(numbers))       # [1, 1, 2, 3, 4, 5, 6, 9]
print(min(numbers))          # 1
print(max(numbers))          # 9
print(sum(numbers))          # 31
print(numbers.count(1))      # 2 (how many times 1 appears)

# Slicing
print(numbers[2:5])   # [4, 1, 5]
print(numbers[:3])    # [3, 1, 4]
print(numbers[::2])   # every other: [3, 4, 5, 2]
