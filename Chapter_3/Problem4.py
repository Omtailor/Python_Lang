# Replace double space from problem with 3 single spaces.
sent="Today is  a beautiful day!"
print(sent.replace("  ", "   "))
print(sent) # Since strings are immutable, no changes are made in original string. 
