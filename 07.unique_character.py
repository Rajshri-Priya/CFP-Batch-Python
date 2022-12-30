# Write a function that takes in a string and returns a set of all the unique characters in the string.S
def unique_characters(string):
    return set(string)  # use the set constructor to create a set of all the unique characters in the string


string = "hello world"
unique_chars = unique_characters(string)
print(unique_chars)  # {'l', 'h', 'o', 'e','', 'w', 'r', 'd'}
