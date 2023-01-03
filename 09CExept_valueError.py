class ValueError(Exception):
    def __init__(self, value):
        self.value = value
    

def greet(name):
    if not isinstance(name, str):
        raise ValueError("Invalid input: not a string.")
    return f"Hello, {name}!"

try:
    result = greet(123)
except ValueError as e:
    print(e)
