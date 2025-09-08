class Point:
    # Constructor to initialize x and y coordinates
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the '+' operator to add two Point objects
    def __add__(self, other):
        # Returns a new Point whose coordinates are the sum of the two points
        return Point(self.x + other.x, self.y + other.y)

    # Overloading the 'str' operator to print the point in a readable format
    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Creating two Point objects
p1 = Point(2, 3)
p2 = Point(4, 5)

# Adding two Point objects using the overloaded '+' operator
p3 = p1 + p2  # This calls p1.__add__(p2)

print(p3)  # Output: Point(6, 8)

# This is possible because the + operator in Python is just syntactic sugar for calling the __add__ method.
# a + b → calls a.__add__(b)

# a - b → calls a.__sub__(b)

# a * b → calls a.__mul__(b)

# a / b → calls a.__truediv__(b)

# a == b → calls a.__eq__(b)
# ...and so on.

# So when Python sees p1 + p2, it checks whether p1 (the left operand) has the method __add__. Since you defined it, Python calls it automatically.
