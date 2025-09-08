# Write a program to mine a log file and check whether it contains python or not

with open("log.txt", "r") as f:
    content = f.read()
    if("Python" in content):
        print("Python found in text")
    else:
        print("Python not found in text")
    