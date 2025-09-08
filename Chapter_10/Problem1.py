# Create Class Programmmer for storing Information of Few Programmers working at Microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self, name, language, Position, Salary, company):
        self.name = name
        self.language = language
        self.Salary = Salary
        self.Position = Position
        self.company = company
        
om = Programmer("Om Tailor,", " Full Stack + AI,", " SWE Intern", 150000, ", Microsoft")
print(om.name, om.language, om.Salary, om.Position, om.company)