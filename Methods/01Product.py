# using instance variable ,instance method ,class variable,class method and static method

class Product:
    # Class variable
    tax_rate = 0.18

    def __init__(self, name, price):        # constructor
        self.name = name        # instance variable
        self.price = price

    # Instance method(get(),set()for instance or obj)
    def get_total_price(self):
        return self.price * (1 + self.tax_rate)

    # Class method
    @classmethod
    def set_tax_rate(cls, rate):
        cls.tax_rate = rate

    # Static method
    @staticmethod
    def is_on_sale(name):
        return name.lower().endswith('sale')

product1 = Product('Shirt', 20)
product2 = Product('Pants', 30)

print("Total price: ", product1.get_total_price())  # instance method called
print("Total price: ", product2.get_total_price())  

Product.set_tax_rate(0.2)  # class method callled
print("Total price after set tax rate: ", product1.get_total_price())  
print("Total price after set tax rate: ", product2.get_total_price())  

print("Is product is on sale: ", Product.is_on_sale('Shirt'))  # static method call
print("Is product is on sale: ", Product.is_on_sale('ShirtSale'))  
