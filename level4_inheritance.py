# Level 4 - Topic 2: Inheritance
# A child class inherits attributes and methods from a parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):  # override parent method
        print(f"{self.name} says: Woof!")

    def fetch(self):  # new method only for Dog
        print(f"{self.name} fetches the ball!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

dog = Dog("Rex")
cat = Cat("Whiskers")

dog.speak()   # Rex says: Woof!
cat.speak()   # Whiskers says: Meow!
dog.eat()     # Rex is eating. (inherited from Animal)
dog.fetch()   # Rex fetches the ball!

# isinstance() checks if object is of a type
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True (Dog IS-A Animal)
print(isinstance(cat, Dog))     # False

# super() - call parent's method
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        super().__init__(name)  # call Dog's (Animal's) __init__
        self.color = color

    def describe(self):
        print(f"{self.name} is a {self.color} Golden Retriever.")

golden = GoldenRetriever("Buddy", "golden")
golden.speak()     # Buddy says: Woof! (from Dog)
golden.describe()  # Buddy is a golden Golden Retriever.
