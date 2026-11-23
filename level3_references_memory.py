# Level 3 - Topic 2: References & Memory
# In Python, variables are labels (references) pointing to objects

import sys

# Two variables can point to same object
a = [1, 2, 3]
b = a             # b is an alias, NOT a copy
print(a is b)     # True - same object in memory
print(id(a) == id(b))  # True - same memory address

b.append(4)
print(a)  # [1, 2, 3, 4] - a is affected!

# To create a true copy:
c = a.copy()
print(a is c)     # False - different objects
c.append(5)
print(a)  # [1, 2, 3, 4] - a is NOT affected

# Small integers are cached (-5 to 256)
x = 100
y = 100
print(x is y)   # True (Python caches small ints)

x = 1000
y = 1000
print(x is y)   # False (larger ints not cached)

# Reference counting - Python tracks how many labels point to an object
lst = [1, 2, 3]
print(sys.getrefcount(lst))  # at least 2 (lst + argument)

# When no references remain, memory is freed (garbage collection)
def show_memory():
    temp = [0] * 1000  # created
    return "done"      # temp goes out of scope -> freed

show_memory()
