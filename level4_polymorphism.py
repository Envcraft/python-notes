# Level 4 - Topic 4: Polymorphism
# Same interface (method name), different behavior per class

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def describe(self):
        print(f"I am a {self.__class__.__name__} with area {self.area():.2f}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Polymorphism: same code works for all shapes
shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]

for shape in shapes:
    shape.describe()
# I am a Circle with area 78.54
# I am a Rectangle with area 24.00
# I am a Triangle with area 12.00

total = sum(shape.area() for shape in shapes)
print(f"Total area: {total:.2f}")

# Duck typing - if it has the method, we can use it
class Star:              # doesn't inherit from Shape
    def area(self):
        return 42.0      # fake area

for obj in shapes + [Star()]:
    print(obj.area())    # works as long as area() exists
