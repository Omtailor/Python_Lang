# Program to print multiplication table of n in reverse order

n = int(input("Enter number of which multiplication table to print: "))
for i in range (1,11):
    print(f"{n} X {11-i} = {n*(11-i)}")

"""
n = int(input("Enter the number to print its multiplication table in reverse order: "))
for i in range(10, 0, -1):
    print(f"{n} X {i} = {n * i}")
"""