# define a superclass
class super_class:
    pass
    # attributes and method definition


# inheritance
class sub_class(super_class):
    pass
    # attributes and method of super_class
    # attributes and method of sub_class


class Animal:
    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)


# create an object of the subclass
labrador = Dog()

# access superclass attribute and method
labrador.name = "Rohu"
labrador.eat()

# call subclass method
labrador.display()

# is-a relationship
# Car is a Vehicle
# Apple is a Fruit
# Cat is an Animal

# Method Overriding in Python Inheritance


class Animal:
    # attributes and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()

# The super() Method in Python Inheritance


class Animal:
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()

        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

labrador.eat()

# # Python Multi-Level inheritance
#
# # class class1:
# #     <class-suite>
# # class class2(class1):
# #     <class suite>
# # class class3(class2):
# #     <class suite>
#
# # Python Multiple inheritance
#
# # class Base1:
# #     <class -suite >
# #
# # class Base2:
# #     <class -suite >
# #
# # class BaseN:
# #     <class -suite >
# #
# # class Derived(Base1, Base2, ......BaseN):
#     <class -suite >


# Uses of Inheritance

# Since a child class can inherit all the functionalities of the parent's class, this allows code reusability.

# Once a functionality is developed, you can simply inherit it.
# No need to reinvent the wheel. This allows for cleaner code and easier to maintain.

# Since you can also add your own functionalities in the child class,
# you can inherit only the useful functionalities and define other required features.
