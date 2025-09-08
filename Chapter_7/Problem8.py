"""Write a program to print following star pattern:
*
**
***"""

n = int(input("Write a number till which star pattern to be printed: "))
for i in range(1, n+1):
    print("*"*i)
