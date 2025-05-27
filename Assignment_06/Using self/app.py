class Student:
    def __init__(self, name, marks):
        self.name = name       
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)

# Creating objects
student1 = Student("Ayesha", 99)
student2 = Student("Zainab", 92)

# Displaying student details
student1.display()
print()  
student2.display()