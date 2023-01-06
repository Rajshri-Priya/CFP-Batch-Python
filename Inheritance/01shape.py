class Shape:
    def __init__(self, name):
        self.name = name
    
    def get_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")      
        self.radius = radius
    
    def get_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width
    
    def get_area(self):
        return self.length * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    
    def get_area(self):
        return 0.5 * self.base * self.height

circle = Circle(5)
print(circle.get_area())

rectangle = Rectangle(10, 5)
print(rectangle.get_area())

triangle = Triangle(10, 5)
print(triangle.get_area())




