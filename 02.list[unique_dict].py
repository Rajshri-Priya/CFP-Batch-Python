# That takes in a list of dictionaries and returns a new list of dictionaries containing only the dictionaries with unique values.

def unique_dicts(dicts):
    # result = []
    result = [d for d in dicts if len(set(d.values())) == len(d.values())]  # by using list comprehension
    # for d in dicts:
    #     # check if the values in the dictionary are unique
    #     if len(set(d.values())) == len(d.values()):
    #         result.append(d)
    return result


dicts = [{"a": 1, "b": 2}, {"a": 1, "b": 3}, {"a": 2, "b": 2}, {"a": 3, "b": 3}]
unique = unique_dicts(dicts)
print(unique)  # [{"a": 1, "b": 2}, {"a": 1, "b": 3}]
