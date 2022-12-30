dict1 = {'a':1, 'b':2, 'e':3, 'f':4}
dict2 = {'c':3, 'd':4, 'a':1, 'b':2}

def dict_union(dict1,dict2):
    # dict3 = dict1.copy()
    dict1.update(dict2)
    return dict1


print("union of dict1 and dict2: ", dict_union(dict1,dict2))
