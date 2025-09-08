# Write Python program to print multiplication table of a given number.


def table(n):
    for i in range(1, 11):
        print(f"{n} X {i} = {n*i}")


n = int(input("Enter number of which table to print: "))
table(n)
