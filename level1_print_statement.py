# Level 1 - Topic: Print Statement
# Comprehensive guide to Python's built-in print() function

# 1. Basic Printing
print("Hello, World!")          # Prints text string
print(42)                       # Prints integers
print(3.14159)                  # Prints floating-point numbers
print(True)                     # Prints booleans

# 2. Printing Multiple Arguments
name = "Ravi"
role = "Developer"
print("Name:", name, "Role:", role)   # Default separates with a single space

# 3. Custom Separator ('sep' parameter)
# By default, sep=" "
print("Python", "Django", "Flutter", sep=" | ")    # Python | Django | Flutter
print("2026", "11", "23", sep="-")                # 2026-11-23
print("apple", "banana", "cherry", sep=", ")       # apple, banana, cherry
print("no", "spaces", sep="")                      # nospaces

# 4. Custom Ending ('end' parameter)
# By default, end="\n" (newline)
print("Loading", end="...")
print(" Done!")                 # Output on same line: Loading... Done!

for i in range(5):
    print(i, end=" ")           # 0 1 2 3 4
print()                         # Empty print() moves cursor to next line

# 5. String Formatting with print()
age = 25
# 5a. f-strings (Recommended)
print(f"My name is {name} and I am {age} years old.")

# 5b. str.format()
print("Item: {}, Cost: ${:.2f}".format("Book", 19.5))

# 5c. Concatenation vs Arguments
print("Hello " + name)          # String concatenation (requires str types)
print("Age:", age)              # Argument passing (automatically converts to str)

# 6. Escape Characters inside print()
print("Line 1\nLine 2")         # \n = New line
print("Column 1\tColumn 2")     # \t = Tab
print("He said, \"Hello!\"")    # \" = Escaped quote
print("C:\\Users\\Path")        # \\ = Escaped backslash

# 7. Flushing Output ('flush' parameter)
# flush=True forces immediate output buffer clearing (useful in timers/progress bars)
print("Processing...", end=" ", flush=True)
print("Completed!", flush=True)

# 8. Redirecting Output ('file' parameter)
# By default, file=sys.stdout. Can direct to sys.stderr or a file:
import sys
print("Standard output stream", file=sys.stdout)
print("Standard error stream (warning/error)", file=sys.stderr)
