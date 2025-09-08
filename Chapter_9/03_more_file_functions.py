f = open("file_for_CHP_9.txt")

# lines = f.readlines()
# print(lines, type(lines)) # Prints entire line as a list.

# line1 = f.readline()
# print(line1, type(line1))  # Prints entire line 1 as a list.

# line2 = f.readline()
# print(line2, type(line2))  # Prints entire line 2 as a list.

# line3 = f.readline()
# print(line3, type(line3))  # Prints entire line 3 as a list.

# line4 = f.readline()
# print(line4, type(line4))  # Prints entire line 4 as a list.

# line5 = f.readline()
# print(line5 == "")  # Prints True since Line 5 is empty.

# More efficient way to print lines:
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
    
f.close()


