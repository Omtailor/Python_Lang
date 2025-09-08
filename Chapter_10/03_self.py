class Employee:  # An Employee is a class here.
    language = "Python"
    salary = 120000000000000000

    def __init__(self, name):
        self.name = name  # Initialize name attribute

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}.")

    def greet(self):
        if self.name:
            print(f"Have a nice day! {self.name}.")
        else:
            print("Have a nice day!")

    # @staticmethod
    # def greet():
    #     print("Good Morning") # Since any object property is not used. @staticmethod can be used.


om = Employee("Om Tailor")
om.language = "Java"  # Java will be printed.
om.getInfo()

om.name = "Om Tailor"
om.greet()  # om.greet == Employee.greet(om)