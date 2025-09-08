# Write a program to greet user with Good day using functions.

n = int(input("Enter number of users to greet: "))

def greet():
    name = input("Enter your Name: ")
    print(f"Good Day, {name}")
    print("Thanks for coming!")


for i in range(1, n + 1):
    greet()
