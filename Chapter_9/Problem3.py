# Write a program to generate multiplication tables from 2 to 20 and write it in different files. Place these files in a folder

def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
        print(table) # If this is not written, tables will be written to the file but not in the console.
    
    with open(f"tables/table_{n}", "w") as f:
        f.write(table)   
        
for i in range (2,21):
    generateTable(i)