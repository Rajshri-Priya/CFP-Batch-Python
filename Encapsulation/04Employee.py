class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

# create a new Employee object
employee = Employee("Rajshri", 50000)

# try to change the salary to a negative value
employee.set_salary(-1000)

# print the current salary
print("Current salary:", employee.get_salary())

# change the salary to a valid value
employee.set_salary(60000)

# print the current salary
print("Current salary:", employee.get_salary())
