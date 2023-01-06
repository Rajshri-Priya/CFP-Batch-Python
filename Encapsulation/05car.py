# car problem in which we used private attributes 

class Car:
    def __init__(self, make, model, year):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__odometer_reading = 0
    
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_year(self):
        return self.__year
    
    def get_odometer_reading(self):
        return self.__odometer_reading
    
    def set_odometer_reading(self, reading):
        if reading >= self.__odometer_reading:
            self.__odometer_reading = reading
        else:
            print("You can't roll back an odometer!")

# create a new Car object
my_car = Car("Toyota", "Camry", 2020)

# print the make, model, and year
print("Make:", my_car.get_make())
print("Model:", my_car.get_model())
print("Year:", my_car.get_year())

# try to set the odometer reading to a lower value
my_car.set_odometer_reading(5000)
print("Odometer reading:", my_car.get_odometer_reading())

# set the odometer reading to a higher value
my_car.set_odometer_reading(10000)
print("Odometer reading:", my_car.get_odometer_reading())
