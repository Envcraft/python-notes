# Level 3 - Topic 4: Iterators
# An iterator is an object that produces one value at a time

# Any iterable (list, string, range) can give an iterator
fruits = ["apple", "banana", "cherry"]
it = iter(fruits)      # get an iterator

print(next(it))  # apple
print(next(it))  # banana
print(next(it))  # cherry
# print(next(it))  # StopIteration - no more items

# A for loop does this automatically
for fruit in fruits:
    print(fruit)

# enumerate() - gives index + value
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: cherry

# zip() - pair up items from multiple iterables
names = ["Alice", "Bob", "Charlie"]
scores = [90, 85, 92]

for name, score in zip(names, scores):
    print(f"{name}: {score}")
# Alice: 90
# Bob: 85
# Charlie: 92

# Custom iterator class
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

for n in Countdown(5):
    print(n, end=" ")  # 5 4 3 2 1
print()
