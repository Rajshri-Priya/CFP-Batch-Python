# Write a function that takes in a list of sets and returns a new set containing all the elements that are present in all the sets in the list.

# take list of set and give intersection no
def intersection(sets):
    # use set comprehension to create a set containing all the elements in the sets that are present in all the sets
    result = {x for s in sets for x in s if all(x in t for t in sets)}
    # all()---return true or false check condition element present in list or not.
    return result


sets = [{1, 2, 3}, {2, 3, 4}, {3, 4, 5}]
intersection_set = intersection(sets)
print(intersection_set)  # {3}