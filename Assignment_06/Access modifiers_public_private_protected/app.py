class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # public
        self._salary = salary     # protected
        self.__ssn = ssn          # private

    def show_info(self):
        print("Inside class:")
        print("Name:", self.name)
        print("Salary:", self._salary)
        print("SSN:", self.__ssn)


# Creating an object
emp = Employee("Alara", 50000, "123-45-6789")

# Accessing variables from outside the class
print("\nAccessing from outside the class:")

# Public - accessible
print("Public (name):", emp.name)

# Protected - technically accessible but should be treated as internal
print("Protected (_salary):", emp._salary)

# Private - will raise AttributeError if accessed directly
try:
    print("Private (__ssn):", emp.__ssn)
except AttributeError as e:
    print("Private (__ssn): Cannot access directly:", e)

# Accessing private using name mangling (not recommended, but possible)
print("Private via name mangling (_Employee__ssn):", emp._Employee__ssn)