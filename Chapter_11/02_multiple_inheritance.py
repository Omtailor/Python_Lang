class Employee:
    company = "Google"
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print(f"The name of Employee is {self.name}, salary is {self.salary}, and he is working at {self.company}")


class Coder:
    def __init__(self, language):
        self.language = language
    
    def coding(self):
        print(f"{self.name} codes in {self.language}")


class Programmer(Employee, Coder):   # multiple inheritance
    company = "Amazon"
    
    def __init__(self, name, salary, language):
        Employee.__init__(self, name, salary)   # call Employee __init__
        Coder.__init__(self, language)          # call Coder __init__
    
    def info(self):
        print(f"The name is {self.name}, proficient in {self.language}, salary is {self.salary}, and is working at {self.company}")


# Create Employee object
a = Employee("Om Tailor", 1200000000000000000000000)
a.show()

# Create Programmer object
b = Programmer("Ravi", 90000000000000000000000, "Java")
b.show()     # from Employee
b.info()     # from Programmer
b.coding()   # from Coder
