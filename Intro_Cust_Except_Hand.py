# define custom exceptions by creating a new class that is derived from the built-in Exception class
'''
Syntax:-
# CustomError is a user-defined error which inherits from the Exception class
class CustomError(Exception):
    ...
    pass

try:
   ...

except CustomError:
'''

# user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")
    