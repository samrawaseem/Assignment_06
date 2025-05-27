class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"Woof! My name is {self.name}.")

# Creating objects
dog1 = Dog("Tommy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Calling instance method
dog1.bark()
dog2.bark()
