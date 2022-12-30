# create a set of integer type
student_id = {112, 114, 116, 118, 115}
print('Student ID:', student_id)

# create an empty set
empty_set = set()

# create an empty dictionary
empty_dictionary = {}

# check data type of empty_set
print('Data type of empty_set:', type(empty_set))

# check data type of dictionary_set
print('Data type of empty_dictionary', type(empty_dictionary))

# Duplicate Items in a Set
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)  # {8, 2, 4, 6}

# Add Items to a Set
numbers = {21, 34, 54, 12}
print('Initial Set:', numbers)
# using add() method
numbers.add(32)
print('Updated Set:', numbers)

# Update Python Set
# The update() method is used to update the set with items other collection types (lists, tuples, sets, etc)
# return only unique values
vowels = {'a', 'e'}
list1 = ['i', 'o', 'u']
vowels.update(list1)
print(vowels)

# Remove an Element from a Set
# We use the discard() method to remove the specified element from a set

languages = {'C', 'C++', 'Python', 'HTML', 'CSS'}
print('Initial Set:', languages)
# remove 'HTML' from a set
removedValue = languages.discard('HTML')
print('Set after remove():', languages)

# Iterate Over a Set
fruits = {"Apple", "Peach", "Mango"}
# for loop to access each fruits
for fruit in fruits:
    print(fruit)

# Find Number of Set Elements
even_numbers = {2, 4, 6, 8}
print('Set:', even_numbers)
# find number of elements
print('Total Elements:', len(even_numbers))  # len() will use to find length of set

# Union of Two Sets
# The union of two sets A and B include all the elements of set A and B.

# We use the | operator or the union() method to perform the set union operation.
A = {1, 3, 5}
B = {0, 2, 4}
# perform union operation using |
print('Union using |:', A | B)
# perform union operation using union()
print('Union using union():', A.union(B))

# Set Intersection
# The intersection of two sets A and B include the common elements between set A and B.

# we use the & operator or the intersection() method to perform the set intersection operation.
A = {1, 3, 5}
B = {1, 2, 3}
# perform intersection operation using &
print('Intersection using &:', A & B)
# perform intersection operation using intersection()
print('Intersection using intersection():', A.intersection(B))

# Difference between Two Sets
# The difference between two sets A and B include elements of set A that are not present on set B.

# We use the - operator or the difference() method to perform the difference between two sets.
A = {2, 3, 5}
B = {1, 2, 6}
# perform difference operation using &
print('Difference using &:', A - B)
# perform difference operation using difference()
print('Difference using difference():', A.difference(B))

# Set Symmetric Difference
# The symmetric difference between two sets A and B includes all elements of A and B without the common elements.

# we use the ^ operator or the symmetric_difference() method to perform symmetric difference between two sets.
A = {2, 3, 5}
B = {1, 2, 6}
# perform difference operation using &
print('using ^:', A ^ B)
# using symmetric_difference()
print('using symmetric_difference():', A.symmetric_difference(B))

# Check if two sets are equal
# We can use the == operator to check whether two sets are equal or not
A = {1, 3, 5}
B = {3, 5, 1}
# perform difference operation using &
if A == B:
    print('Set A and Set B are equal')
else:
    print('Set A and Set B are not equal')