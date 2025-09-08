class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


# Employee inherits from Person (Level 1 → Level 2)
class Employee(Person):
    def __init__(self, name, salary):
        super().__init__(name)   # call Person __init__
        self.salary = salary

    def show_employee(self):
        print(f"Employee Name: {self.name}, Salary: {self.salary}")


# Programmer inherits from Employee (Level 2 → Level 3)
class Programmer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)   # call Employee __init__
        self.language = language

    def show_programmer(self):
        print(f"Programmer Name: {self.name}, Salary: {self.salary}, Language: {self.language}")


# --- Usage ---
# Create Programmer object (has access to all levels)
p = Programmer("Om Tailor", 100000, "Python")

p.show_name()        # from Person
p.show_employee()    # from Employee
p.show_programmer()  # from Programmer
