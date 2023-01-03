class RangeError(Exception):
    def __init__(self, value): # constructor
        self.value = value

def add(x, y):
    if not (0 <= x <= 100) or not (0 <= y <= 100):
        raise RangeError("Number is outside of the allowed range.")
    return x + y

try:
    result = add(150, 100)
    print(result)
except RangeError as e:
    print(e)
