# Label the program in problem 4 with comments.


# This program prints all files from certain folder.
# Write a python program to print contents of directory using os module. Search online for the function that does that.

import os

# Prompt the user to enter a directory path
path = input("Enter the path of the directory: ")

try:
    # Get the list of all files and directories
    dir_contents = os.listdir(path)
    
    print(f"Contents of '{path}':")
    for item in dir_contents:
        print(item)
except FileNotFoundError:
    print(f"The directory '{path}' does not exist.")
except PermissionError:
    print(f"Permission denied to access '{path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
