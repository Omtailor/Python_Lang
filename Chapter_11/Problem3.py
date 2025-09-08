# Create a class Employee and add salary and increment properties to it.

class Employee:
    salary = 512
    increment = 25
    
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary) - 1)*100
        
        
e = Employee()
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 640
print(e.increment)