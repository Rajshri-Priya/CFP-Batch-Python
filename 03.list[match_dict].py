def find_target_values(dicts, target):
    # use list comprehension to create a list of dictionaries that have at least one key-value pair with a value equal to the target value
    result = [d for d in dicts if any(value == target for value in d.values())]
    return result


dicts = [{"a": 1, "b": 2}, {"a": 3, "b": 4}, {"a": 5, "b": 6}]
target = 4
target_dicts = find_target_values(dicts, target)
print(target_dicts)  # [{"a": 3, "b": 4}]
