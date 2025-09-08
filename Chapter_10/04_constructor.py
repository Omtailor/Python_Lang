class Employee: 
    language = "Python"
    salary = 120000000000000000
    
    def __init__(self, name, language, salary): # Starting with underscore in Python are called Dunder Methods. _init_ is automatically called
        self.name = name
        self.language = language
        self.salary = salary
    
om = Employee("Om Tailor", "Javascript", 1200000000000000000)
om.name = "Om Tailor"
print(om.name, om.language, om.salary)

# rohan = Employee()
# rohan.name = "Rohan Robinson"
# print(rohan.name, rohan.salary, rohan.language)

# Rohan needs to be comment out since, _init_ is for all objects, not only one subject. For only one object will show error.
# A constructor is a special function in a class that runs automatically when an object is created and is used to initialize the object’s variables.