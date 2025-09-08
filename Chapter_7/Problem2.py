"""Write a program to greet all person given in list.
l = ["Om", "Rohit", "Messi"]"""

l = ["Om", "Rohit Sharma", "Messi"]
for i in range(len(l)):
    print(f"Good Morning, {l[i]}")

# Greet only those people whose name starts with 'S'
l2 = ["Harry", "Om", "Soham", "Sachin", "Rahul"]
"""for i in range(len(l2)):
    if l2[i].startswith("S"):
        print(f"Good Morning, {l2[i]}")"""

# More optimized solution:
for name in l2:
    if(name.startswith("S")):
        print(f"Good Morning, {name}")

