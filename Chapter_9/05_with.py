# f = open("file_for_CHP_9.txt")
# data = f.read()
# print(data)
# f.close()

# Same can be written using with statement as below:
with open("file_for_CHP_9.txt") as f:
    print(f.read())

# We dont need to explicityly close the file