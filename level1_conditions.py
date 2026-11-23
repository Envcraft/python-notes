# Level 1 - Topic 4: Conditions (if / elif / else)

age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")
# Output: Adult

# Inline condition (ternary)
score = 75
result = "Pass" if score >= 50 else "Fail"
print(result)  # Pass

# Combining conditions
temperature = 22
is_sunny = True

if temperature > 20 and is_sunny:
    print("Great day for a walk!")

# Checking membership
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list")  # prints this

# Checking for None
value = None
if value is None:
    print("No value set")
