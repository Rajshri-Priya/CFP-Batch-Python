class Shape:
    def calculate_area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width

def get_areas(shapes):
    for shape in shapes:
        print(shape.calculate_area())

circles = [Circle(5), Circle(3)]
rectangles = [Rectangle(4, 6), Rectangle(2, 4)]
get_areas(circles)
get_areas(rectangles)
