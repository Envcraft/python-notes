# Level 2 - Topic 4: Dictionaries
# Key-value pairs, like a real dictionary (word -> definition)

person = {
    "name": "Alice",
    "age": 30,
    "city": "Delhi"
}

# Access values by key
print(person["name"])         # Alice
print(person.get("age"))      # 30
print(person.get("phone", "N/A"))  # N/A (default if missing)

# Modify / add
person["age"] = 31
person["email"] = "alice@example.com"
print(person)

# Remove
del person["city"]
removed = person.pop("email")
print(removed)  # alice@example.com

# Iterate
for key in person:
    print(key, "->", person[key])

for key, value in person.items():
    print(f"{key}: {value}")

# Check if key exists
print("name" in person)   # True
print("phone" in person)  # False

# Useful methods
print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 31])

# Nested dictionary
student = {
    "name": "Bob",
    "grades": {"math": 90, "science": 85}
}
print(student["grades"]["math"])  # 90
