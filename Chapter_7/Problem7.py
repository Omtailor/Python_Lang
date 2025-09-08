# Write a program to print following star pattern
"""For n = 3
  *
 ***
******"""

"""For n = 5
    *
   ***
  *****
 *******
********** """

n = int(input("Enter number till which star pattern to print: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")  # For proper spacing.
    print("*" * (2 * i - 1), end="")  # For star printing.
    print("")


# end is used to prevent going to new line and do the operations on the same line