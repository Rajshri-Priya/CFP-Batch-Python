class InvalidInputError(Exception):
    def __init__(self, message):
        self.message=message

def reverse_string(input_string):
    if not isinstance(input_string, str):
        raise InvalidInputError("Input must be a string")
    return input_string[::-1]

def main():
    try:
        print(reverse_string("hello"))
        print(reverse_string(123))
    except InvalidInputError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
