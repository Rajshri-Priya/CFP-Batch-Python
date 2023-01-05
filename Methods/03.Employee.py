# using instance variable ,instance method ,class variable,class method and static method

class Employee:
  # Class variable
  raise_amount = 1.05

  def __init__(self, name, salary):
    self.name = name
    self.salary = salary

  # Instance method
  def give_raise(self):
    self.salary *= self.raise_amount

  # Class method
  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

  # Static method
  @staticmethod
  def is_valid_salary(salary):
    return salary > 0

employee1 = Employee('Raj', 50_000)
employee2 = Employee('jai', 60_000)

employee1.give_raise() # instance mehod call
print("salary: ", employee1.salary)  
print("salary: ", employee2.salary)  

Employee.set_raise_amount(1.1)
employee2.give_raise()
print("salary raised by 1.1: ", employee1.salary)  
print("salary raised by 1.1: ", employee2.salary)  

print(Employee.is_valid_salary(50_000))  
print(Employee.is_valid_salary(-50_000))  