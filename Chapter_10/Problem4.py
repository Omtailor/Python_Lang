# Add a static method in Problem 2 to greet user with "Kem Cho"

# Write a class "calculator" capable of finding square, cube and square root of a number.


class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        return self.n**2

    def cube(self):
        return self.n**3

    def square_root(self):
        return self.n**0.5

    @staticmethod
    def greet():
        print("Kem Cho!!")


n = int(input("Enter number of which operations to perform: "))
operations = calculator(n)
print(operations.greet(), operations.square(), operations.cube(), operations.square_root())

# Constructor is only used to initialize objects. All operations will be done by methods,functions
