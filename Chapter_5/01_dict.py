# Dictionary is a collection of key-value pairs. Like Mapping is being done here.
# Dictionaries are unordered, mutable, indexed, Cannot contain duplicate keys.

marks = {
    "Om": 100,
    "Pratham": 69,
    "Yash": 68
} # Here, Om, Pratham and Yash are keys, thus called indexed whereas marks are values. 
print(marks, type(marks))

print(marks["Om2"]) # Accessed value using keys, example of indexing, Gives error if key is not there.
print(marks.get("Om2")) # Returns none if key is not there.

# Modifying the value of an existing key
marks["Pratham"] = 95  # Changed Pratham's marks

# Adding a new key-value pair
marks["Sneha"] = 88

marks.update({"Pratham:96", "Renuka:89"}) 

# Removing a key-value pair
del marks["Yash"]

# Displaying the updated dictionary
print(marks)

dict = {} # Represents empty dictionary.
print(type(dict))
