friends = ["Apple", "Orange", 5, 6465.0254, False, "Aakash", "Rohan"]

friends.append("Harry") # Prints object at end of string.
print(friends)

num = [1,15,68,79,81,4,23,28,11]
print(sum(num))

num.sort() # Sorts number in ascending order, Here original list will be changed.
print(num)

# num.sort() will sort the list num, but it does not return the sorted list.
# So when you do num1 = num.sort(), you're storing the return value of sort() in num1.
# But the return value of sort() is None. So num1 becomes None.
# Then print(num1) shows: None

# For getting new sorted list. Original list will not be affected.
num1 = sorted(num)
print(num1)
#print(num) 

num.reverse()
print(num) # Prints number in descending to ascending order. 

num.insert(3,11) # Insert 11 at index 3.
print(num)

num2 = [1,22,3,4,55,6,56,75]
print(num2.pop(2)) # Will delete element at index 2 and return the value.
b = num2.count(55)
print(b)

num3 = [12,45,65,445,5,55]
num3.remove(65) # Removes 65 from the list.
print(num3)

concatenated = num + num2
print(concatenated)