# Create on empty dictionary. Allow 4 friends to enter their favourite language as values and use keys as there names. 
# Assume that their names are unique.

friend_lang={}

name1=input("Enter your name: ")
lang1=input("Enter your favourite language: ")

name2=input("Enter your name: ")
lang2=input("Enter your favourite language: ")

name3=input("Enter your name: ")
lang3=input("Enter your favourite language: ")

name4=input("Enter your name: ")
lang4=input("Enter your favourite language: ")

friend_lang[name1]= lang1
friend_lang[name2]= lang2
friend_lang[name3]= lang3
friend_lang[name4]= lang4

print(friend_lang)

# If names of two friends are same then, value entered last/late will be displayed.
# If languages of two friends are same then, no changes, will print in normal way only.