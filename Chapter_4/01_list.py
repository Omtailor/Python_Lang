# A list is containers to store values of any datatype.
# Strings cannot be changed but lists can be changed, thus strings are mutable.
# Lists can be indexed just like string. 
# Slicing in lists is same as that of strings.

friends= ["Apple", "Orange", 5, 6465.0254, False, "Aakash", "Rohan"]
print(friends[0])
friends[0]= "Grapes" # Modification of Lists
print(friends[0])
print(friends[1:4])
print(friends[1:7:3])


# Same can be done with strings too.
a = "Tailor"
# a[3]=n, This is not possible in strings.
print(a[2])