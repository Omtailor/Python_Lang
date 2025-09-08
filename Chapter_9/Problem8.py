# Write program to check whether a file is identical and matches the content of another file

with open("this.txt", "r") as f:
    content_copy_1 = f.read()
    
with open("copy.txt", "r") as f:
    content_copy_2 = f.read()
    
if (content_copy_1 == content_copy_2):
    print("Files are identical")
else:
    print("Files are not identical")