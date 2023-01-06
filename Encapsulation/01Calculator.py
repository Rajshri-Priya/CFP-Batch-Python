class Calculator:
    def __init__(self, value1, value2):
        self.__value1 = value1 # private variable
        self.__value2 = value2 # private variable
    
    def __add(self): # private method
        return self.__value1 + self.__value2
    
    def get_sum(self):
        return self.__add()

calculator = Calculator(5, 10)
print(calculator.get_sum())