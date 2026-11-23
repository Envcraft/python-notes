# Level 5 - Topic 1: Decorators
# A decorator wraps a function to add behavior without changing its code

import time

# Simple decorator
def shout(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@shout
def greet(name):
    return f"hello, {name}"

print(greet("Alice"))  # HELLO, ALICE

# Practical decorator: timing
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1_000_000)  # slow_sum took 0.0300s

# Decorator with arguments
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()
# Hi!
# Hi!
# Hi!

# Stacking decorators
@timer
@shout
def hello(name):
    return f"hello, {name}"

hello("Bob")  # timed + uppercased
