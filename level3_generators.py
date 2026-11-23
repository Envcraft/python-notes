# Level 3 - Topic 5: Generators
# A generator produces values one at a time using "yield"
# Memory-efficient: doesn't create all values at once

# Regular function returns all at once
def get_squares_list(n):
    return [i ** 2 for i in range(n)]  # all in memory

# Generator function - pauses at each yield
def get_squares_gen(n):
    for i in range(n):
        yield i ** 2  # pauses here, resumes on next()

# Using a generator
gen = get_squares_gen(5)
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# Or iterate with for loop
for sq in get_squares_gen(5):
    print(sq, end=" ")  # 0 1 4 9 16
print()

# Infinite generator (can't do this with a list!)
def infinite_counter(start=0):
    n = start
    while True:
        yield n
        n += 1

counter = infinite_counter(10)
for _ in range(5):
    print(next(counter), end=" ")  # 10 11 12 13 14
print()

# Generator expression (like list comprehension but lazy)
gen_expr = (x ** 2 for x in range(10))
print(sum(gen_expr))  # 285 - computed on the fly

# Real use case: reading a huge file line by line
def read_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
# Only one line in memory at a time!
