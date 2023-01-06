class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

class Manager(Employee):
    def __init__(self, name, salary, bonus):  
        super().__init__(name, salary)    # inherit from super class name and salary
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

employee1 = Employee("raj", 50000)  # class employee
print(employee1.get_salary())

manager1 = Manager("Shri", 60000, 10000)       # class Manager
print(manager1.get_salary())
