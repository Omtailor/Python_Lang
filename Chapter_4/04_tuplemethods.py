a = (45,5,655,45,18,"Rohan", "Om")
no = a.count(45) # Checks no of occurences of 45 in tuple.
print(no)

no1 = a.index("Om")  # Output: 2, Returns the index of the specified value.
print(no1)

no2 = len(a)  # Output: 7
print(no2)

x, y, z, w, u, name1, name2 = a
print(name1)  # Output: Rohan, Assigns elements of the tuple to variables.

print("Rohan" in a)  # Output: True

print(a[0:3])   # Output: (45, 5, 655), All Slicing rules applicable here.

# Tuples can contain other tuples, often used in database-style records or coordinate data.
person = ("Rohan", (25, "Engineer"), "India")

print(tuple([1, 2, 3]))  # Output: (1, 2, 3), Convert lists or other iterable data types into tuples.

tuple1 = (1,23,46,28)
tuple2 = (45,454,958)
concatenated = tuple1 + tuple2 # Prints concatenated tuple
print(concatenated)

t = (4, 1, 7)
print(max(t))  # Output: 7, Prints largest value of tuple.
print(min(t))  # Output: 1, Prints largest value of tuple.

t1 = (1, 2, 3)
print(sum(t1))  # Output: 6, Print sum of all numeric values in the tuple.