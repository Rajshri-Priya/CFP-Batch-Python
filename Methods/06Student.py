# using instance variable ,instance method ,class variable,class method and static method

class Student:
  # Class variable
  enrollment = 0

  def __init__(self, name, major, gpa):
    self.name = name
    self.major = major
    self.gpa = gpa
    Student.enrollment += 1

  # Instance method
  def on_honor_roll(self):
    return self.gpa >= 3.5

  # Class method
  @classmethod
  def get_enrollment(cls):
    return cls.enrollment

  # Static method
  @staticmethod
  def is_gpa_valid(gpa):
    return 0 <= gpa <= 4.0

student1 = Student('Raj', 'Computer Science', 4.7)
student2 = Student('Tanish', 'Biology', 3.5)

print(student1.on_honor_roll())  # Output: True
print(Student.get_enrollment())  # Output: 2
print(Student.is_gpa_valid(3.5))  # Output: True
print(Student.is_gpa_valid(-0.1))  # Output: False
