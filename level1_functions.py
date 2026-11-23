# Level 1 - Topic 6: Functions

# Basic function definition
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Hello, Alice!
greet("Bob")    # Hello, Bob!

# Function with return value
def add(a, b):
    return a + b

result = add(3, 4)
print(result)  # 7

# Default parameter values
def greet_with_title(name, title="Mr."):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")           # Hello, Mr. Smith!
greet_with_title("Smith", "Dr.")    # Hello, Dr. Smith!

# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([3, 1, 7, 2, 9])
print(low, high)  # 1 9

# Keyword arguments
def describe(name, age, city):
    print(f"{name}, age {age}, from {city}")

describe(age=30, city="Delhi", name="Ravi")  # order doesn't matter
