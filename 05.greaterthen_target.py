# dict having greater value then target value:

d = {'a': 100, 'b': 200, 'c': 300}
# Target value 
t = 150


def greater_dict(d):
    # Dictionary to store result 
    res = {key: value for key, value in d.items() if value > t}
    # Iterate over dictionary and check for greater than target value 
    # for key, value in d.items(): 
    #     if value > t: 
    #         res[key] = value 
    return res


# Print result dictionary     
print("dict having greater value then target value: ", greater_dict(d))
