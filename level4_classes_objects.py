# Level 4 - Topic 1: Classes & Objects
# A class is a blueprint; an object is an instance of that blueprint

class Dog:
    # Class variable - shared by all instances
    species = "Canis lupus familiaris"

    # __init__ is called when you create an object
    def __init__(self, name, age):
        # Instance variables - unique to each object
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says: Woof!")

    def describe(self):
        print(f"{self.name} is {self.age} years old.")

    # String representation
    def __str__(self):
        return f"Dog({self.name}, {self.age})"

# Create objects (instances)
dog1 = Dog("Rex", 3)
dog2 = Dog("Buddy", 5)

dog1.bark()         # Rex says: Woof!
dog2.describe()     # Buddy is 5 years old.

print(dog1.name)    # Rex
print(dog2.age)     # 5
print(Dog.species)  # Canis lupus familiaris
print(dog1)         # Dog(Rex, 3)

# Objects are independent
dog1.name = "Max"
print(dog1.name)   # Max
print(dog2.name)   # Buddy - unchanged
