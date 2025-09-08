# Write a program to mine a log file and check whether it contains python or not. Also find the line number.

with open("log.txt", "r") as f:
    content = f.readlines() # f.readlines() reads file line by line not entirely
    
    lineno = 1
    for line in content:
        if("python" in line):
            print(f"Yes, python is present. Line no: {lineno}")
            break
        lineno += 1

    else:
        print("python is not present")
    