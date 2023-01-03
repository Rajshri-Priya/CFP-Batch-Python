class InvalidInputError(Exception):
    def __init__(self, message):
        self.message = message

def get_number_from_user():
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please try again.")

try:
    result = get_number_from_user()
except InvalidInputError as e:
    print(e.message)
