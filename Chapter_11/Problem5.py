# Write a class vector representing vector of n dimension. Overload the + and * operator which calculates sum and dot product of them


class Vector3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Overload + operator (vector addition)
    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    # Overload * operator (dot product)
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    # Nicely print vector
    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


# Example usage
v1 = Vector3D(1, 2, 3)
v2 = Vector3D(4, 5, 6)

print("v1 + v2 =", v1 + v2)  # (5, 7, 9)
print("v1 · v2 =", v1 * v2)  # 32
