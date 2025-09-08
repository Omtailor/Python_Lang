# What will be the length of following set: s=Set() 
# s.add (20)
# s.add (20.0)
# s- add ("20") = length of s after these operations?

s=set() 
s.add(20)
s.add(20.0)
s.add("20") 
l=len(s)
print(l)

# Length will be 2 after all operations.
