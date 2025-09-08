# Calculation of factorial using for loop.

'''def factorial():
    a = int(input("Enter a number of which factorial to found: "))
    fact = 1
    for i in range (1,a+1):
        fact = fact*i
    print("Factorial of given number is: ", fact )

factorial()'''

# Calculation of factorial using recursion

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter number of which factorial to calculate: "))
result = fact(n)
print(f"Factorial of {n} is {result}")