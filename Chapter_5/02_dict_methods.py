marks = {"Om": 100, "Pratham": 69, "Yash": 68}
# "Om", "Pratham", and "Yash" are keys (used to index the dictionary).
# 100, 69, 68 are their corresponding values.

print(marks.keys())
# Returns a view of all keys in the dictionary.
# Output: dict_keys(['Om', 'Pratham', 'Yash'])

print(marks.values())
# Returns a view of all values in the dictionary.
# Output: dict_values([100, 69, 68])

print(marks.items())
# Returns a view of all key-value pairs (as tuples).
# Output: dict_items([('Om', 100), ('Pratham', 69), ('Yash', 68)])

print(marks.pop("Yash"))
# Removes and returns the value for key "Yash".
# Output: 68
# Now marks becomes: {'Om': 100, 'Pratham': 69}

marks["Rahul"] = 85  # Adding a new key-value pair for demonstration
print(marks.popitem())
# Removes and returns the last inserted key-value pair.
# Output: ('Rahul', 85)
# Now marks becomes: {'Om': 100, 'Pratham': 69}

marks.clear()
# Removes all items from the dictionary.
print(marks)
# Output: {}

# Let's repopulate the dictionary for further operations
marks = {"Om": 100, "Pratham": 69}

new_marks = marks.copy()
# Returns a shallow copy of the dictionary.
print(new_marks)
# Output: {'Om': 100, 'Pratham': 69}

print(marks.setdefault("Om", 90))
# "Om" exists, so it returns its value and does not update it.
# Output: 100

print(marks.setdefault("Jay", 75))
# "Jay" doesn't exist, so it's added with value 75.
# Output: 75

print(marks)
# Output: {'Om': 100, 'Pratham': 69, 'Jay': 75}
