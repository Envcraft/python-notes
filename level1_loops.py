# Level 1 - Topic 5: Loops

# for loop - iterate over a sequence
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# apple
# banana
# cherry

# range() - generate numbers
for i in range(5):        # 0, 1, 2, 3, 4
    print(i, end=" ")
print()

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i, end=" ")
print()

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step=2)
    print(i, end=" ")
print()

# while loop - repeat while condition is true
count = 0
while count < 3:
    print("count:", count)
    count += 1

# break - exit loop early
for n in range(10):
    if n == 5:
        break
    print(n, end=" ")
print()  # 0 1 2 3 4

# continue - skip current iteration
for n in range(6):
    if n == 3:
        continue
    print(n, end=" ")
print()  # 0 1 2 4 5
