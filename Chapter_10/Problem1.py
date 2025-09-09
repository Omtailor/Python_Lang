# Create Class Programmmer for storing Information of Few Programmers working at Microsoft
class Programmer:
    company = "TCS"
    def __init__(self, name, language, Position, Salary, company):
        self.name = name
        self.language = language
        self.Salary = Salary
        self.Position = Position
        self.company = company
        
om = Programmer("Om Tailor,", " Choding,", " Majdoor", 150, ", TCS")
print(om.name, om.language, om.Salary, om.Position, om.company)
