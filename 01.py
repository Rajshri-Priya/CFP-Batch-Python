# Write a function that takes in a list of sets as arguments and returns the union of all the sets in the list.

def union_of_sets(sets):
    result = set()
    for s in sets:
        result |= s
    return result


sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
print(union_of_sets(sets))



