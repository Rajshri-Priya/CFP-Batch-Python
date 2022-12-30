# that takes in a list of sets  and returns a new set containing all the elements that are present in all the sets in the list.
def all_common_elements(sets):
    result = sets[0]
    for s in sets[1:]:
        result &= s
    return result


sets = [{1, 2, 3}, {3, 4, 2}, {3, 4, 2}]
print(all_common_elements(sets))
