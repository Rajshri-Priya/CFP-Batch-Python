# that takes in a list of sets and returns a new list containing all the elements that are present in at least two of the sets in list.

def common_elements(sets):
    result = []
    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            result.append(sets[i] & sets[j])
        return result

sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
print(common_elements(sets))