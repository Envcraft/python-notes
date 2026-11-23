# Level 3 - Topic 3: Functions as Objects
# In Python, functions are "first-class objects"
# They can be stored in variables, passed as arguments, returned

# Assign function to a variable
def greet(name):
    return f"Hello, {name}!"

say_hi = greet          # no parentheses - we're assigning the function
print(say_hi("Alice"))  # Hello, Alice!

# Pass function as argument (higher-order function)
def apply(func, value):
    return func(value)

def double(x):
    return x * 2

def square(x):
    return x ** 2

print(apply(double, 5))   # 10
print(apply(square, 5))   # 25

# Built-in higher-order functions
nums = [1, 2, 3, 4, 5]
doubled = list(map(double, nums))     # apply double to each
print(doubled)  # [2, 4, 6, 8, 10]

evens = list(filter(lambda x: x % 2 == 0, nums))  # keep even
print(evens)    # [2, 4]

# Lambda - anonymous (unnamed) one-line function
multiply = lambda a, b: a * b
print(multiply(3, 4))   # 12

# Sorting with a key function
words = ["banana", "apple", "cherry", "date"]
print(sorted(words, key=len))  # sort by length: ['date', 'apple', 'banana', 'cherry']

# Return a function from a function
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

triple = make_multiplier(3)
print(triple(7))  # 21
