def greet(name, ending = "Thank you"):
    print("Good Day", name)
    print(ending)

greet("Om", "Welcome") # Since we assigned ending parameter with "Welcome", it will print "Welcome"
greet("Om") # Since we didn't assigned ending parameter, it will print Thank you"
# Here, "Thank you" acts as default parameter.