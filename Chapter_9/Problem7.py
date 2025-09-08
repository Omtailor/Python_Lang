# Write program to make copy of file this.txt

with open("this.txt", "r") as f:
    content_copy = f.read() # f.read() reads entire file, not line by line

with open("copy.txt", "w") as f:
    f.write(content_copy)
    