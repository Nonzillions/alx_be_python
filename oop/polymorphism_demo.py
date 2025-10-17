import math

class Shape:
    def area(self):
        # This method must be overridden by subclasses
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        # Area formula for rectangle: length × width
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        # Area formula for circle: π × r²
        return math.pi * (self.radius ** 2)