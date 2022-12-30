# Write a function that takes in a list of sets as arguments and returns the intersection of all the sets in the list.
def intersection_of_sets(sets):
    result = sets[0]
    for s in sets[1:]:
        result &= s
        return result


sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
print(intersection_of_sets(sets))
