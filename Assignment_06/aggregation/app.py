class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: Department has a reference to Employee

    def show_department_info(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()  # Access Employee's method

# Create an Employee object (exists independently)
emp1 = Employee("Alara", "Software Engineer")

# Create a Department object and pass the Employee object
dept = Department("IT", emp1)

# Show department info which includes employee details
dept.show_department_info()
