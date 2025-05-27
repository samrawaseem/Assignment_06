from abc import ABC, abstractmethod

# Abstract base class
class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

# Concrete class
class Rectangle(Shape):
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Creating an object of Rectangle
rect = Rectangle(5, 3)
print("Area of Rectangle:", rect.area())

