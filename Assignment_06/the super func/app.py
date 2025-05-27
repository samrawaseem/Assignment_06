class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person initialized with name: {self.name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent constructor
        self.subject = subject
        print(f"Teacher initialized with subject: {self.subject}")

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Subject: {self.subject}")

# Creating an object of Teacher
t = Teacher("Ms. Samra", "Pharmacology")
t.display_info()
