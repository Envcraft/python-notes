# Level 2 - Topic 3: Tuples
# Ordered, IMMUTABLE (cannot change after creation)

point = (3, 7)
rgb = (255, 128, 0)

# Access just like lists
print(point[0])  # 3
print(rgb[-1])   # 0

# Unpack into variables
x, y = point
print(f"x={x}, y={y}")  # x=3, y=7

r, g, b = rgb
print(f"Red={r}, Green={g}, Blue={b}")

# Tuples cannot be changed
# point[0] = 10  # This would raise: TypeError

# Single-element tuple needs a trailing comma
single = (42,)
print(type(single))  # <class 'tuple'>
not_tuple = (42)
print(type(not_tuple))  # <class 'int'>

# Common use: returning multiple values from a function
def get_dimensions():
    return 1920, 1080  # returns a tuple

width, height = get_dimensions()
print(f"{width}x{height}")  # 1920x1080

# Tuple methods
nums = (1, 2, 3, 2, 4, 2)
print(nums.count(2))   # 3
print(nums.index(3))   # 2 (first position of value 3)
