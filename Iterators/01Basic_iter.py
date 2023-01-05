print("\n**************LIST ITERATION**************************\n")
# list iteration
numbers = [1, 2, 3, 4, 5]
for number in numbers:
  print(number)  # Output: 1 2 3 4 5

print("\n****************STRING ITERATION************************\n")
# Iterating over a string
string = 'abcdefg'
for character in string:
  print(character)  # Output: 'a' 'b' 'c' 'd' 'e' 'f' 'g'

print("\n**************DICTIONARY ITERATION**************************\n")
# Iterating over a string
person = {'first_name': 'Raj', 'last_name': 'shri', 'age': 30}
for key in person:
  print(key, person[key])  # Output: 'first_name' 'John' 'last_name' 'Doe' 'age' 30

print("\n**************RANGE ITERATION**************************\n")
# range iteration
for i in range(5):
  print(i) 

print("\n**************ITERATING TO LIST SIMULTANEOUSLY**************************\n")
# Iterating over two lists simultaneously
names = ['Raj', 'Shri', 'Priya']
ages = [20, 21, 22]
for name, age in zip(names, ages):
  print(name, age)  

