# Level 2 - Topic 7: Comprehensions
# A concise way to create lists, dicts, and sets

# --- List Comprehension ---
# Traditional way:
squares = []
for n in range(1, 6):
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Comprehension way (same result, one line):
squares = [n ** 2 for n in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With a condition (filter)
evens = [n for n in range(10) if n % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

# Transform strings
words = ["hello", "world", "python"]
upper_words = [w.upper() for w in words]
print(upper_words)  # ['HELLO', 'WORLD', 'PYTHON']

# --- Dictionary Comprehension ---
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# --- Set Comprehension ---
nums = [1, 2, 2, 3, 3, 3]
unique_squares = {n ** 2 for n in nums}
print(unique_squares)  # {1, 4, 9}

# --- Generator Expression (lazy, memory efficient) ---
total = sum(n ** 2 for n in range(1000000))  # doesn't build a list
print(total)
