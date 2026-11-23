# Level 6 - Topic 2: Modules & Packages
# Modules = .py files; Packages = folders with __init__.py

# --- Importing standard library modules ---
import math
print(math.pi)          # 3.141592653589793
print(math.sqrt(25))    # 5.0
print(math.ceil(4.2))   # 5

# Import specific things
from math import floor, factorial
print(floor(4.9))       # 4
print(factorial(5))     # 120

# Import with alias
import datetime as dt
today = dt.date.today()
print(today)

from datetime import timedelta as td
tomorrow = today + td(days=1)
print(tomorrow)

# --- Useful standard library modules ---
import os
print(os.getcwd())           # current working directory
print(os.path.exists("hello_world.py"))  # True if file exists

import random
print(random.randint(1, 10))  # random integer 1-10
print(random.choice(["a", "b", "c"]))   # random element

import json
data = {"name": "Alice", "age": 30}
json_str = json.dumps(data)   # dict -> JSON string
print(json_str)               # {"name": "Alice", "age": 30}
back = json.loads(json_str)   # JSON string -> dict
print(back["name"])           # Alice

import collections
counter = collections.Counter(["a", "b", "a", "c", "a", "b"])
print(counter)                # Counter({'a': 3, 'b': 2, 'c': 1})
print(counter.most_common(2)) # [('a', 3), ('b', 2)]

# --- if __name__ == "__main__" ---
# This code only runs when file is executed directly (not when imported)
if __name__ == "__main__":
    print("This file is being run directly.")
