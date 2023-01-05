class Person:
    def __init__(self, name, hobbies):
        self.name = name
        self.hobbies = hobbies

    def add_hobby(self, hobby):
        self.hobbies.append(hobby)

person = Person("Bob", ["reading", "cooking"])
person.add_hobby("gardening")
print(f"Hobbies: {person.hobbies}")
