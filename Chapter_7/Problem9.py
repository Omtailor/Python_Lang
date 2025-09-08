# Program to print following star pattern
"""
***
* *
***
"""

n = int(input("Enter number till which hollow star pattern to print: "))
for i in range (1, n+1):
    if(i==1 or i==n):
        print("*"*n)
    else:
        print("*" + " "*(n-2) + "*")
