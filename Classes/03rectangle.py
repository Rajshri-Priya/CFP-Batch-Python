class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

rectangle = Rectangle(10, 5)
print(f"Area: {rectangle.get_area()}")
print(f"Perimeter: {rectangle.get_perimeter()}")
