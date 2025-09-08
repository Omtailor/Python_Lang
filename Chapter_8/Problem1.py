# Write program using functions to find greatest of three numbers


# Using in-built function max:
'''def greatest(a, b, c):
    maximum = max(a, b, c)
    return maximum


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
x = greatest(a, b, c)
print(f"Maximum of {a}, {b} and {c} is {x}")'''

# Using our own logic
def greatest(a, b, c):
    if a >= b and a >= c:
        print(f"{a} is greatest")
    elif b >= a and b >= c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
greatest(a, b, c)
