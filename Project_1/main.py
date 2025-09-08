"""
1 for Snake
-1 for Water
0 for Gun
"""

import random

# Assign values
computer = random.choice([1, 0, -1])
yourstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
yourDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = yourDict[yourstr]

print(f"You chose {reverseDict[you]}")
print(f"Computer chose {reverseDict[computer]}")

# Draw condition
if computer == you:
    print("It's a draw!")

# Win/Lose conditions without using 'or'
elif (computer == -1 and you == 1):
    print("You Win!")  # Snake drinks water

elif (computer == 0 and you == -1):
    print("You Win!")  # Water damages gun

elif (computer == 1 and you == 0):
    print("You Win!")  # Gun kills snake

else:
    print("You Lose!")


