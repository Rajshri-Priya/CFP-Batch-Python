# handle invalid input:
class InvalidInputError(Exception):
    def __init__(self, message):        # constructor
        self.message = message

def square(number):
    """isinstance() function returns True if the object is specified types, and it will not match then return False. 
        syntax:
        isinstance(obj, class)

        Parameters : 
        obj : The object that need to be checked as a part of class or not.
        class : class/type/tuple of class or type, against which object is needed to be checked.
        Returns : True, if object belongs to the given class/type if single class is passed or any of the class/type if tuple of class/type is passed, else returns False. Raises

        TypeError: if anything other than mentioned valid class type. 
    """
    if not isinstance(number, int) or number < 0:   
        raise InvalidInputError("Input must be a positive integer")
    return number ** 2

try:
    result = square(5)
    print(result)
except InvalidInputError as e:
    print(e.message)
