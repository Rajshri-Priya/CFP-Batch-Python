class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_circumference(self):
        return 2 * 3.14 * self.radius

circle = Circle(5, "red")
print(f"Area: {circle.get_area()}")
print(f"Circumference: {circle.get_circumference()}")
