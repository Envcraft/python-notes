# Level 5 - Topic 4: Type Hints
# Optional annotations that say what types a function expects/returns
# Python doesn't enforce these at runtime - they're for readability and tools

# Basic type hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b

def is_adult(age: int) -> bool:
    return age >= 18

print(greet("Alice"))  # Hello, Alice!
print(add(3, 4))       # 7
print(is_adult(20))    # True

# Hinting with collections
from typing import List, Dict, Tuple, Optional

def sum_numbers(numbers: List[int]) -> int:
    return sum(numbers)

def get_scores() -> Dict[str, int]:
    return {"Alice": 90, "Bob": 85}

def get_point() -> Tuple[int, int]:
    return (3, 7)

# Optional - value can be the type OR None
def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)  # returns None if not found

print(find_user(1))   # Alice
print(find_user(99))  # None

# Python 3.10+ shorthand (no need for Optional)
def find_user_modern(user_id: int) -> str | None:
    users = {1: "Alice"}
    return users.get(user_id)

# Type aliases
Coordinate = Tuple[float, float]

def distance(p1: Coordinate, p2: Coordinate) -> float:
    return ((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2) ** 0.5

print(distance((0, 0), (3, 4)))  # 5.0
