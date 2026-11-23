# Level 6 - Topic 1: Exceptions
# Handle errors gracefully instead of crashing

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Multiple exception types
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer")
        return None
    except TypeError:
        print("Value must be a string or number")
        return None

print(safe_int("42"))    # 42
print(safe_int("abc"))   # 'abc' is not a valid integer -> None
print(safe_int(None))    # Value must be a string or number -> None

# else and finally
def read_file(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    else:
        print("File opened successfully!")  # runs if NO exception
        f.close()
    finally:
        print("This always runs (cleanup).")  # always runs

read_file("nonexistent.txt")

# Raise exceptions
def set_age(age):
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Error: {e}")  # Error: Age cannot be negative: -5

# Custom exception
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Balance {balance} < withdrawal {amount}")
        self.balance = balance
        self.amount = amount

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount

try:
    withdraw(100, 200)
except InsufficientFundsError as e:
    print(e)  # Balance 100 < withdrawal 200
