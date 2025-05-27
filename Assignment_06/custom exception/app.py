class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        self.message = message
        super().__init__(self.message)

# Function that checks age and raises exception if invalid
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Age must be at least 18.")
    else:
        print(f"Age {age} is valid.")

# Using try...except to handle the custom exception
try:
    check_age(16)  # This should raise the exception
except InvalidAgeError as e:
    print(f"Caught an error: {e}")

try:
    check_age(21)  # This should be valid
except InvalidAgeError as e:
    print(f"Caught an error: {e}")


#     - A custom error InvalidAgeError is created for ages below 18.
# - check_age(age) raises this error if age < 18, otherwise prints that the age is valid.
# - The code checks age 16 (shows error) and age 21 (shows valid).
# - try...except is used to catch and print the custom error message, so the program keeps running.