# Level 2 - Topic 1: Strings

text = "Hello, Python!"

# Accessing characters (indexing)
print(text[0])    # H  (first character)
print(text[-1])   # !  (last character)

# Slicing
print(text[0:5])  # Hello
print(text[7:])   # Python!
print(text[:5])   # Hello

# Common string methods
print(text.upper())          # HELLO, PYTHON!
print(text.lower())          # hello, python!
print(text.replace("Python", "World"))  # Hello, World!
print(text.split(", "))      # ['Hello', 'Python!']
print("  hello  ".strip())   # hello (removes spaces)
print(text.startswith("Hello"))  # True
print(text.count("l"))       # 3

# f-strings (formatted strings) - most modern way
name = "Ravi"
age = 25
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")

# String length
print(len(text))  # 14

# Check if substring exists
print("Python" in text)  # True
