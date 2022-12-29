# Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples.
def sum_of_elements(list_of_tuples):
    result = [sum(tup) for tup in list_of_tuples]  # list comprihension used
    print("The sum of all the elements of each tuple stored inside a list: ", result)


List1 = [(1, 2), (2, 3), (3, 4)]
sum_of_elements(List1)
List2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
sum_of_elements(List2)
