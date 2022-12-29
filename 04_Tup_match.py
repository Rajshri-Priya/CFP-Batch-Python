# Write a Python program to check if a specified element presents in a tuple of tuples.
original_list = (('Red', 'White', 'Blue'), ('Green', 'Pink', 'Purple'), ('Orange', 'Yellow', 'Lime'))


def check_element(tuple_of_tuples, element):
    for tup in tuple_of_tuples:
        if element in tup:
            return True
    return False


print(check_element(original_list, 'White'))
print(check_element(original_list, 'Olive'))
