# using instance variable ,instance method ,class variable,class method and static method

class Car:
  # Class variable
  sale_price = 0.9

  def __init__(self, make, model, price):
    self.make = make
    self.model = model
    self.price = price

  # Instance method
  def get_discounted_price(self):
    return self.price * self.sale_price

  # Class method
  @classmethod
  def set_sale_price(cls, price):
    cls.sale_price = price

  # Static method
  @staticmethod
  def is_luxury_car(make):
    return make in ['Mercedes', 'BMW', 'Porsche']

car1 = Car('Toyota', 'Camry', 20_000)
car2 = Car('Mercedes', 'S-Class', 100_000)

print("Total discounted price: ", car1.get_discounted_price())  
print("Total discounted price: ", car2.get_discounted_price()) 
Car.set_sale_price(0.8)
print("Total discounted price: ", car1.get_discounted_price()) 
print("Total discounted price: ", car2.get_discounted_price()) 

print(Car.is_luxury_car('Toyota'))  
print(Car.is_luxury_car('Mercedes'))  
