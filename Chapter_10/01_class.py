class Employee:  # An Employee is a class here.
    language = "Python"
    salary = 120000000000000000


om = Employee()  # Object is created here.
om.name = "Om Tailor"
print(om.name, om.language, om.salary)

rohan = Employee()  # Object is created here.
rohan.name = "Rohan Roro Robinson"
print(rohan.name, rohan.language, rohan.salary)

# om and rohan are objects here
# language and salary are class attributes as they directly belong to class.
# name is an object attribute as it is associated with object. Also called instance attribute.
