# Using tuple as an element in a list

list_of_tuples = [(1, 2), (3, 4), (5, 6)]
flattened_list = [item for tuple in list_of_tuples for item in tuple]
print(flattened_list)  # Output: [1, 2, 3, 4, 5, 6]
