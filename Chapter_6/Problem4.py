# Write whether given username contain less than 10 characters or not.

name = input("Enter your name:")
if len(name) < 10:
    print("Your name contains less than 10 characters.")
else:
    print("Your name has greater than or equal to 10 characters.")
