# Write a program to print sum of first n natural numbers using while loop.

n = int(input("Enter a number till which sum of natural numbers to be found: "))
i = 0
sum = 0
while(i<=n):
    sum = sum + i
    i = i+1

print("Sum is:", sum)