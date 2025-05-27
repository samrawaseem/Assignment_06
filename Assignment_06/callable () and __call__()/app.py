class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create an instance with factor 5
multiplier = Multiplier(5)

# Check if the object is callable
print(callable(multiplier))  # Output: True

# Call the object like a function
result = multiplier(10)
print(result) 