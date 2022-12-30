# ordered collection
# key:value
# key must be unique

# Create dictionary with keys and values
print("\n---Create dictionary with keys and values---\n")
capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ", capital_city)

# Add Elements to a Python Dictionary
print("\n---Add Elements to a Dictionary---\n")
capital_city["Japan"] = "Tokyo"
print("Updated Dictionary: ", capital_city)

# Change Value of Dictionary
print("\n---Change Value of Dictionary---\n")
student_id = {111: "Raj", 112: "Shri", 113: "Priya"}
print("Initial Dictionary: ", student_id)
student_id[112] = "lakshmi"     # Change Value of Dictionary
print("Updated Dictionary: ", student_id)

# Accessing Elements from Dictionary
print("\n--- Accessing Elements from Dictionary through index---\n")
print(student_id[111])
print(student_id[113])


# Removing elements from Dictionary
print("\n---Removing elements from Dictionary at[111] by using del()---\n")
# The del statement to remove an element from the dictionary.
print("Initial Dictionary: ", student_id)
del student_id[111]
print("Updated Dictionary ", student_id)

# Dictionary Membership Test
# Membership Test for Dictionary Keys
print("\n---Membership Test for Dictionary Keys---\n")
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
print("Dictionary for membership Test: ", {key: value for key, value in squares.items()})
print(1 in squares)  # prints True
print(2 not in squares)  # prints True
# membership tests for key only not value
print(49 in squares)  # prints false


# Iterating Through a Dictionary
print("\n---Iterating Through a Dictionary---\n")
squares = {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
for i in squares:
    print(squares[i])
