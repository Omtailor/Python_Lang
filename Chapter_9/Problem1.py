# Write a program to read text from a given file and find out whether it contains word "twinkle"

# with open("file_for_CHP_9.txt") as f:
#     line = f.readline()
#     while line != "":
#         if "twinkle" in line.lower():
#             print("Twinkle is detected")
#             break
#         else:
#             print("Twinkle not detected")
#         line = f.readline()  #  Now it updates the line properly


# Most efficient code using content. Will check for entire file not individual lines.

with open("file_for_CHP_9.txt") as f:
    content = f.read().lower()
    if "twinkle" in content:
        print("Twinkle is detected")
    else:
        print("Twinkle not detected")
