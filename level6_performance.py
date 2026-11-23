# Level 6 - Topic 6: Performance
# Writing efficient Python code

import time
import sys
from functools import lru_cache

# --- Timing code ---
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__}: {(end-start)*1000:.2f}ms")
        return result
    return wrapper

# --- List vs Generator memory ---
list_version = [x ** 2 for x in range(1_000_000)]
gen_version = (x ** 2 for x in range(1_000_000))

print(f"List size: {sys.getsizeof(list_version):,} bytes")
print(f"Generator size: {sys.getsizeof(gen_version)} bytes")

# --- Caching with lru_cache ---
# Without cache: recalculates same values repeatedly
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

@timer
def calc_fib():
    return fib(100)  # very fast with cache

calc_fib()
print(f"fib(100) = {fib(100)}")

# --- String concatenation ---
@timer
def slow_concat(n):
    result = ""
    for i in range(n):
        result += str(i)  # creates new string each time
    return result

@timer
def fast_concat(n):
    return "".join(str(i) for i in range(n))  # much faster

slow_concat(10_000)
fast_concat(10_000)

# --- Use built-ins (they're implemented in C) ---
numbers = list(range(100_000))

@timer
def manual_sum():
    total = 0
    for n in numbers:
        total += n
    return total

@timer
def builtin_sum():
    return sum(numbers)  # ~10x faster

manual_sum()
builtin_sum()
