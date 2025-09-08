def greet(name, ending):
    print("Good Day,", name)
    print(ending)
    return "OK BHAI, DONE"

a = greet("Harry", "Thank you")
b = greet("OM", "Thank you")
c = greet("Sundar Pichai", "Thanks")
print(a,b,c)

# Here, name and ending are arguements. We have passed the arguements to function.
# If return is not written, None will come while printing a,b,c
# Since return is written, if any variable calls function return value will be there.