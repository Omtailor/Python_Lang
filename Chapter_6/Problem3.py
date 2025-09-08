# A spam comment is defined as text containing keywords:
# "Make a lot of money", "buy now", "subsribe this", "click this". Write a program to detect these spams

program = input("Enter program to detect spams if any: ")
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"
if (p1 in program) or (p2 in program) or (p3 in program) or (p4 in program):
    print("Warning, Spam Detected!")
else:
    print("Your are safe and free from spam :)")
