# Write a Python program to convert a given list of tuples to a list of lists.
def conversion(list_of_tuples):
    converted_list = [list(tup) for tup in list_of_tuples]
    print("To convert a given list of tuples to a list of lists: ", converted_list)


list1 = [(1, 2), (2, 3), (3, 4)]
conversion(list1)
list2 = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
conversion(list1)
