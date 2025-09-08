class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(
            f"The name of Employee is {self.name}, salary is {self.salary}, and he is working at {self.company}"
        )


class Programmer(Employee):  # inherits Employee
    company = "Amazon"

    def __init__(self, name, salary, language):
        super().__init__(name, salary)  # call Employee __init__
        self.language = language

    def info(self):
        print(
            f"The name is {self.name}, proficient in {self.language}, salary is {self.salary}, and is working at {self.company}"
        )


# Create Employee object
a = Employee("Om Tailor", 12000000000000000000000000000000000000)
a.show()

# Create Programmer object
b = Programmer("Ravi", 90000000000000000000000, "Java")
b.show()  # inherited method
b.info()  # Programmer's own method

# Since Programmer inherits Employee, you should still call the parent constructor to set name and salary. Otherwise, self.name and self.salary don’t exist inside Programmer.

# Super keyword allows you to call methods (like __init__, or any other method) from a parent class (superclass) inside a child class (subclass), without explicitly naming the parent class.


class A:
    def show(self):
        print("Class A method")


class B(A):
    def show(self):
        super().show()  # calls A's show
        print("Class B method")


b = B()
b.show()
