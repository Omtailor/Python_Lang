class Employee:
    # Class attribute 'a'
    a = 1

    @classmethod
    def show(cls):
        # Prints the value of the class attribute 'a'
        print(f"The class attribute of a is {cls.a}")

    @property
    def name(self):
        # Returns the full name by combining first and last name
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        # Splits the input value and sets first and last name
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = Employee()
e.a = 45  # Sets an instance attribute 'a', does not affect the class attribute
e.name = "Om Khan"  # Sets 'fname' to 'Om' and 'lname' to 'Khan' using the setter
print(e.fname, e.lname)  # Prints: Om Khan

e.show()  # Calls the classmethod, prints the class attribute 'a' (which is 1)

