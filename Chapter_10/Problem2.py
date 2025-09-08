# Write a class "calculator" capable of finding square, cube and square root of a number.

class Calculator:
    def __init__(self, n):
        self.n = n
        
    def square(self):
        return self.n**2
        
    def cube(self):
        return self.n**3
        
    def squareroot(self):
        return self.n**0.5
  
n = int(input("Enter number of which operations to perform: "))      
operations = Calculator(n)
print(operations.square(), operations.cube(), operations.squareroot())

# Constructor is only used to initialize objects. All operations will be done by methods,functions
