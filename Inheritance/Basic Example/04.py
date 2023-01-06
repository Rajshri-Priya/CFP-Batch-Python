class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    
class Car(Vehicle):
    def __init__(self, make, model, year, num_wheels):
        super().__init__(make, model, year)      # inherit from super class make ,model,year
        self.num_wheels = num_wheels

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, num_wheels):  # # inherit from super class make ,model,year
        super().__init__(make, model, year)
        self.num_wheels = num_wheels

car1 = Car("Honda", "Accord", 2020, 4)  # instance of class Car
car1.start_engine()

motorcycle1 = Motorcycle("Suzuki", "Hayabusa", 2021, 2)     #  # instance of class Car
motorcycle1.start_engine()
