# Write a program to find whether given name is present in list or not.

friends = ["Apple", "Orange", "Henry", "Hrithik", "Aamir", "Aakash", "Rohan", "Om Shah"]
name = input("Enter your name: ")
check = friends.find(name)
if check == -1:
    print("Not Found")
else:
    print("Your name found")
