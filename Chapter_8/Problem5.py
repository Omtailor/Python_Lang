# Write Pytjon program to print first n lines of following pattern:
"""
***
**
*
"""

# Using for loop
'''
n  = int(input("Enter number till which star pattern to print: "))

for i in range(n, 0 , -1): # For printing reverse pattern do like this, # (n+1, i) wont execute since it counts up
    print("*"*i)
'''

# Using Recursion

def pattern(n):
    if(n==0):
        return 0
    else:
        print("*"*n)
    pattern(n-1)

pattern(5)