# list of sets and returns a new set containing all the elements that are present in an even number of sets in the list.
def even(sets):
    # use set comprehension to create a set containing all the elements in the sets that are present in an even number of sets
    result = {x for s in sets for x in s if sum([1 for t in sets if x in t]) % 2 == 0}
    return result


sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
even_set = even(sets)
print(even_set)  # {2, 4}
