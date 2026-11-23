# Level 1 - Topic 2: Data Types
# Python's built-in data types

# int - whole numbers
count = 10
print(type(count))   # <class 'int'>

# float - decimal numbers
price = 9.99
print(type(price))   # <class 'float'>

# str - text
message = "Hello, Python!"
print(type(message)) # <class 'str'>

# bool - True or False
active = True
print(type(active))  # <class 'bool'>

# NoneType - represents "nothing"
result = None
print(result)        # None
print(type(result))  # <class 'NoneType'>

# Type conversion
num_str = "42"
num = int(num_str)   # str -> int
print(num + 1)       # 43

pi = 3.14
print(int(pi))       # 3  (truncates decimal)
print(str(100))      # "100"
