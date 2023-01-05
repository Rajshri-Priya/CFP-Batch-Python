# Sorting a list of tuples by the second element in each tuple


list_of_tuples = [(2, 'b'), (1, 'a'), (3, 'c')]
sorted_list = sorted(list_of_tuples, key=lambda x: x[1])
print(sorted_list)
