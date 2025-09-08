# Using recursive function find sum of first n natural numbers:


def sum(n):
    summation = 1
    if n == 1:
        return 1
    else:
        summation = n + sum(n - 1)
        return summation


n = int(input("Enter number till which sum to be found: "))
x = sum(n)
print(f"Sum from 1 till {n} is {x}")
