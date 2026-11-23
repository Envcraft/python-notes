# Level 2 - Topic 6: Mutability
# Mutable = can change after creation
# Immutable = cannot change after creation

# IMMUTABLE types: int, float, str, tuple, bool
x = 10
y = x       # y gets a copy of the value
x = 20
print(x, y)  # 20 10 - y is unaffected

name = "Alice"
# name[0] = "B"  # TypeError: strings are immutable

# MUTABLE types: list, dict, set
list_a = [1, 2, 3]
list_b = list_a  # both point to SAME list in memory
list_a.append(4)
print(list_b)    # [1, 2, 3, 4] - list_b also changed!

# To make a true copy of a list:
list_c = list_a.copy()   # or list_a[:]
list_a.append(5)
print(list_c)   # [1, 2, 3, 4] - list_c is unaffected

# Why this matters in functions
def add_item(lst):
    lst.append(99)  # modifies the original!

my_list = [1, 2, 3]
add_item(my_list)
print(my_list)   # [1, 2, 3, 99]

# To avoid mutation, pass a copy
def safe_add(lst):
    lst = lst.copy()
    lst.append(99)
    return lst

original = [1, 2, 3]
new_list = safe_add(original)
print(original)  # [1, 2, 3] - unchanged
print(new_list)  # [1, 2, 3, 99]
