# Write a Python program to calculate the average value of the numbers in a given tuple of tuples.
def calculate_tuple_average(tup):
    result = [sum(x) / len(x) for x in tup] # list comprehension "create a new list based on the values of an existing list"
    return result


tup1 = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
average1 = calculate_tuple_average(tup1)
print("Average value of the numbers of the said tuple of tuples:", average1)


tup2 = ((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
average2 = calculate_tuple_average(tup2)
print("Average value of the numbers of the said tuple of tuples:", average2)
