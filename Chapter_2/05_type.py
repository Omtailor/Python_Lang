# type() function is used to find datatype of given variable in Python
a = 31
b = type(a)
print(b) # Here output will be class <int>

c = 56.27
d = type(c)
print(d) # Here output will be class <float>

e = 'Om Tailor' 
f = type(e)
print(f) # Here output will be class <str>

# If anything is under double quotes/single quotes then it is a string.

# We can also change the type of Function
l = "31.2"
m = type(l)
print(m) # Here output will be class <str>

n = "31.2"
o = float(n) # String to Float Conversion
p = type(o)
print(p) # Here output will be class <float>

q = 1.2
o = int(q) # Float to int Conversion
r = type(o)
print(r) # Here output will be class <int>

