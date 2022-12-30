def greater_than(sets, target):
    greater = set([x for s in sets for x in s if x > target])

    #Without list Comprehension
    # result = set()  # create an empty set to store the result
    # for s in sets:
    #     # add all the elements in the set that are greater than the target value
    #     result.update([x for x in s if x > target])
    return greater

sets = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}]
target = 7
greater = greater_than(sets, target)
print(greater)  # {8, 9}