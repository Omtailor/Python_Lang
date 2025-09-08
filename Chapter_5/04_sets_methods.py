s = {1, 2, 11 , 28 , 11 , 6, "Tailor", "Kushal"}

s.add(566) # Adds 566 in original set.

s.remove(6)

s.discard(99) # Removes element; no error if not found 

s.pop() # Removes and returns random element, we cannot give input here. 

s1 = s.copy() # Returns a shallow copy

s.intersection({1, 2, 100}) # Output will be {1,2}

s.union({100, 200}) # Outpur will be {1, 2, 11 , 28 , 100 , 6, "Tailor", "Kushal", 200}

s.difference({1, 2}) # Output will be {6, 11, 28, 'Tailor', 'Kushal'}

s.symmetric_difference({1, 2, 100}) # {6, 11, 28, 'Tailor', 'Kushal', 100}

{1, 2}.issubset(s) # Output in True/False
s.issuperset({1, 2}) # # Output in True/False.

s.isdisjoint({999}) # # Output in True/False, True if no common elements

s.remove(11) # Removes 11 from set.
p=len(s) # Gives length of set.
print(p)

s.clear() # Clears all elements. 
print(s)

s2={2, 3, 4, "Kushal"}
print(s.union(s2))
print(s.intersection(s2))


