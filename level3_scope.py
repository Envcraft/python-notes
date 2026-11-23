# Level 3 - Topic 1: Scope
# Where a variable is visible/accessible (LEGB rule)
# L = Local, E = Enclosing, G = Global, B = Built-in

# Global scope - defined at module level
greeting = "Hello"

def say_hello():
    # Local scope - only visible inside this function
    name = "Alice"
    print(greeting)  # can read global variable
    print(name)

say_hello()
# print(name)  # NameError: name is not defined here

# Modifying a global variable inside a function
count = 0

def increment():
    global count  # declare intent to modify global
    count += 1

increment()
increment()
print(count)  # 2

# Enclosing scope (closure)
def outer():
    message = "outer message"

    def inner():
        print(message)  # inner can see outer's variables

    inner()

outer()

# nonlocal - modify enclosing variable
def counter():
    n = 0
    def increment():
        nonlocal n
        n += 1
        return n
    return increment

c = counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3
