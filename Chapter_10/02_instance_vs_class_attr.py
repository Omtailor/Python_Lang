class Employee:  # An Employee is a class here.
    language = "Python"
    salary = 120000000000000000


om = Employee()
om.name = "Om Tailor"
om.language = "Java"  # Java will be printed.
print(om.name, om.language, om.salary)

rohan = Employee()
rohan.name = "Rowdy Rohan"
rohan.language = "C++"  # C++ will be printed
print(rohan.name, rohan.language, rohan.salary)

# Object Attributes have preference over Class Attributes during assignment and retrieval
