# Create a class with class attribute a, create an object from it and set 'a' directly using object.a=o. Does this change class attribute?


class Demo:
    a = 4


o = Demo()
print(o.a)  # Prints 4 since instance attribute is absent.
o.a = 0  # Set an attribute a on the instance o
print(o.a)  # Prints 0 since instance attribute is present
print(Demo.a)  # Method to print class attribute even when instance attribute is present.

# So class attribute will not be changed, it will remain same
# If instance attribute is present, it will be given prefrence during assignment and retrieval.
