# In Python, input function always returns string by default

a = input("Enter first Number: ")
b = input("Enter second Number: ")
print ("Sum is ", a+b) # Here, they will concatenate like 28 and 11 will be 2811 not 39

c = int(input("Enter first Number: "))
d = int(input("Enter second Number: "))
print ("Sum is ", c+d) # Here, they will concatenate like 28 and 11 will be 39 not 2811

