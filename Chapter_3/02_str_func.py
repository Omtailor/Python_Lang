name = 'om tailor'

p = len(name) # Gives length of string
print(p)

# startswith and endswith string- Ans in True or False only.
print(name.endswith("ilor")) # Checks whether strings end with specified value given by user in function.
print(name.startswith("Ta")) # Checks whether strings starts with specified value given by user in function, It is Case Sensitive.

print(name.capitalize()) # Only capitalizes first letter of string, Nothing is capitalized after spaces by this function in string.

name.upper()      # Output: 'OM TAILOR'. Converts all characters to uppercase.

name.lower()      # Output: 'om tailor'. Converts all characters to lowercase.

name.title()      # Output: 'Om Tailor'. Converts the first character of each word to uppercase.

name_with_spaces = "  om tailor  "
name_with_spaces.strip()  # Output: 'om tailor'. Removes leading and trailing whitespace.

name.replace("tailor", "designer")  # Output: 'om designer'. Replaces substring with another.

name.split()      # Output: ['om', 'tailor']. Splits the string into a list of words using whitespace (or a specific separator).

words = ['om', 'tailor']
' '.join(words)   # Output: 'om tailor'. Joins a list of strings into a single string using a separator.

name.find("tailor")   # Output: 3. Finds the index of the first occurrence of a substring. Returns -1 if not found.

name.count("o")   # Output: 2. Counts how many times a substring occurs.

name.isalpha()        # Output: False (because of the space)
"omtailor".isalpha()  # Output: True. Checks if all characters are alphabetic or numeric.















