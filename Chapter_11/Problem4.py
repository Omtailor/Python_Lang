class Complex:
    # Constructor to initialize real and imaginary parts
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overloading the '+' operator
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # Overloading the '*' operator (complex multiplication)
    def __mul__(self, other):
        # (a+bi)(c+di) = (ac - bd) + (ad + bc)i
        real_part = self.real * other.real - self.imag * other.imag
        imag_part = self.real * other.imag + self.imag * other.real
        return Complex(real_part, imag_part)

    # Overloading the str() function for readability
    def __str__(self):
        return f"{self.real} + {self.imag}i"
    

# Creating two complex objects
p1 = Complex(2, 3)   # 2 + 3i
p2 = Complex(4, 5)   # 4 + 5i

# Using overloaded operators
p3 = p1 + p2
p4 = p1 * p2

print("Addition:", p3)   # (2+3i) + (4+5i) = 6 + 8i
print("Multiplication:", p4)  # (2+3i)(4+5i) = -7 + 22i
