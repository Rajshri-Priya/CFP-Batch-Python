# Write a function that takes in a list of sets as arguments and returns the difference between the union of all the sets and the intersection of all the sets.

def union_of_sets(sets):
    result = set()
    for s in sets:
        result |= s
    return result


def intersection_of_sets(sets):
    result = sets[0]
    for s in sets[1:]:
        result &= s
        return result


def difference_of_sets(sets):
    union = union_of_sets(sets)
    intersection = intersection_of_sets(sets)
    return union - intersection


sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
print(difference_of_sets(sets))