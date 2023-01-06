from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

triangle = Triangle(5, 10)
rectangle = Rectangle(10, 5)
circle = Circle(5)

print("Area of Triangle: ", triangle.calculate_area())  
print("Area of Rectangle: ", rectangle.calculate_area())  
print("Area of Circle: ", circle.calculate_area())  
