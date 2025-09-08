class Parent:
    def __init__(self, name):
        self.name = name
        print("Parent __init__ called")

    def show(self):
        print(f"Hello, I am {self.name} from Parent class")


class Child(Parent):
    def __init__(self, name, age):
        # Call Parent's __init__ using super()
        super().__init__(name)  
        self.age = age
        print("Child __init__ called")

    def show(self):
        # Call Parent's show() method also
        super().show()  
        print(f"My age is {self.age}, from Child class")


# --- Usage ---
c = Child("Om", 20)
c.show()

# It is used to call a method (including __init__) from the parent class inside a child class.
# It avoids writing the parent class name explicitly and helps with cleaner multiple/multilevel inheritance.