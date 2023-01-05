# takes a dict and a key, returns a tuple containing the value for specified key &  number of occur of  value in  dict.

def count_occurrences(d, key):
    # use a list comprehension to count the number of occurrences of the value for the specified key in the dictionary
    count = sum([1 for x in d.values() if x == d[key]])  # 1 is value count in dict
    return (d[key], count)


d = {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1}
key = "a"
occurrences = count_occurrences(d, key)
print(occurrences)  # (1, 3)
