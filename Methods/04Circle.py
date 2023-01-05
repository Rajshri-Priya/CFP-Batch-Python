# using instance variable ,instance method ,class variable,class method and static method

class Circle:
  # Class variable
  pi = 3.14

  def __init__(self, radius):
    self.radius = radius

  # Instance method
  def area(self):
    return self.pi * self.radius ** 2

  # Class method
  @classmethod
  def set_pi(cls, new_pi):
    cls.pi = new_pi

  # Static method
  @staticmethod
  def is_valid_radius(radius):
    return radius > 0

circle1 = Circle(5)
circle2 = Circle(6)

print("Area: ", circle1.area())  
print("Area: ", circle2.area())  

Circle.set_pi(3.141)
print("Area pi(3.141): ", circle1.area())  
print("Area pi(3.141): ", circle2.area())  

print(Circle.is_valid_radius(5))  
print(Circle.is_valid_radius(-5))  
