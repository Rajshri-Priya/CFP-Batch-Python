class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat") # Call the super class constructor
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog") # Call the super class constructor
        self.breed = breed

    def make_sound(self):
        print("Bark!")

cat1 = Cat("Kitty", "Siamese", "Ball")
cat1.play()
cat1.make_sound()

dog1 = Dog("Rover", "Labrador")
dog1.make_sound()
