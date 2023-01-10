# lambda function to get the maximum value in a dictionary

get_max_value = lambda d: max(d.values())
print(get_max_value({"a": 1, "b": 2, "c": 3}))  # Output: 3
