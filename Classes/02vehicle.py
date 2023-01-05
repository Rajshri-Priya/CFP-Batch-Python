class Vehicle:
    def __init__(self, make, model, year, wheels):
        self.make = make
        self.model = model
        self.year = year
        self.wheels = wheels

    def display_info(self):
        return f"{self.year} {self.make} {self.model} with {self.wheels} wheels"

vehicle = Vehicle("Ford", "F150", 2020, 4)
print(vehicle.display_info())

