# Write Python program to fill in a letter template given below with name and date.
#   Dear <|Name|>,
#   You are selected!
#   <|Date|> 

# Method 01
#name=input("Enter your name: ")
#date=input("Enter date: ")
#print("Dear",name)
#print("You are selected!")
#print(date)

# Method 2
letter =("""Dear <|Name|>,
You are selected!
<|Date|>""") 

print(letter.replace("<|Name|>", "Om Tailor").replace("<|Date|>", "11 June 2035"))