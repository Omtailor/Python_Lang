# Calculate factorial of given number using for loop

fact = int(input("Enter number of which factorial to found: "))
for i in range(1, fact):
    fact = fact * i
    i = i + 1

print("Factorial of given number is: ", fact)
