# tuples are similar to list but we cannot change it means immutable

# Advantages of Tuple over List
# We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
# Tuples are immutable, iterating through a tuple is faster than with a list. So there is a slight performance boost.
# Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
# If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.



# Different types of tuples
# Empty tuple
my_tuple = ()
print("Empty Tuple : ", my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print("Tup le having integers : ", my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print("Tuple with mixed datatypes : ", my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print("Nested tuple : ", my_tuple)

# accessing tuple elements using indexing
letters = ("p", "r", "o", "g", "r", "a", "m", "i", "z")
print("Element at [0] : ", letters[0])  # prints "p"
print("Element at [5]: ", letters[5])  # prints "a"

# accessing tuple elements using negative indexing
letters = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
print("Element at [-1] : ", letters[-1])   # prints 'z'
print("Element at [-3] : ", letters[-3])   # prints 'r'

# accessing tuple elements using slicing
my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
# elements 2nd to 4th index
print(my_tuple[1:4])    # prints ('r', 'o', 'g')
# elements beginning to 2nd
print(my_tuple[:-7])    # prints ('p', 'r')
# elements 8th to end
print(my_tuple[7:])     # prints ('i', 'z')
# elements beginning to end
print(my_tuple[:])      # Prints ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')


# Tuple Methods
my_tuple = ('a', 'p', 'p', 'l', 'e',)
print(my_tuple.count('p'))  # prints 2
print(my_tuple.index('l'))  # prints 3


# Iterating through a Tuple
languages = ('Python', 'C', 'C++')
# iterating through the tuple
for language in languages:
    print(language)


# Check if an Item Exists in Tuple
languages = ('Python', 'C', 'C++')
print('HTML' in languages)    # False
print('Python' in languages)    # True