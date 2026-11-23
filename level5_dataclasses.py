# Level 5 - Topic 5: Dataclasses
# Auto-generate __init__, __repr__, __eq__ and more
# Great for classes that mainly hold data

from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float

p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)
p3 = Point(3.0, 4.0)

print(p1)         # Point(x=1.0, y=2.0)  - __repr__ auto-generated
print(p1 == p2)   # True  - __eq__ compares fields
print(p1 == p3)   # False

# Default values
@dataclass
class Person:
    name: str
    age: int = 0
    hobbies: List[str] = field(default_factory=list)  # mutable default needs field()

alice = Person("Alice", 30)
bob = Person("Bob")
alice.hobbies.append("reading")

print(alice)  # Person(name='Alice', age=30, hobbies=['reading'])
print(bob)    # Person(name='Bob', age=0, hobbies=[])

# Frozen dataclass (immutable, like a named tuple)
@dataclass(frozen=True)
class Color:
    r: int
    g: int
    b: int

    def to_hex(self) -> str:
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

red = Color(255, 0, 0)
print(red.to_hex())    # #ff0000
# red.r = 128  # FrozenInstanceError!

# Comparison with order=True
@dataclass(order=True)
class Student:
    grade: int
    name: str

students = [Student(85, "Bob"), Student(92, "Alice"), Student(78, "Charlie")]
print(sorted(students))  # sorted by grade first
