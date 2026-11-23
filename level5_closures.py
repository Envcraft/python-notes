# Level 5 - Topic 2: Closures
# A closure is a function that "remembers" variables from its enclosing scope

# Basic closure
def make_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"  # remembers 'greeting'
    return greet

hello = make_greeting("Hello")
hi = make_greeting("Hi")

print(hello("Alice"))  # Hello, Alice!
print(hi("Bob"))       # Hi, Bob!
print(hello("Charlie"))# Hello, Charlie!

# Counter closure
def make_counter(start=0):
    count = start

    def increment(step=1):
        nonlocal count
        count += step
        return count

    def reset():
        nonlocal count
        count = start

    def get():
        return count

    return increment, reset, get

inc, reset, get = make_counter(10)
print(inc())     # 11
print(inc(5))    # 16
print(get())     # 16
reset()
print(get())     # 10

# Closures vs classes - closures are simpler for small state
def make_adder(n):
    return lambda x: x + n   # lambda closes over n

add5 = make_adder(5)
add10 = make_adder(10)
print(add5(3))   # 8
print(add10(3))  # 13

# View the closure variables
print(add5.__closure__[0].cell_contents)  # 5
