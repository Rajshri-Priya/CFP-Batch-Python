# find even value from dictionary and save in new dictionary
dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}

# new_dic = {}
# for key, value in dic.items():
#     if value % 2 == 0:
#         new_dic[key] = value
        
# print(new_dic)
# another way
def even(dic):
    new_dic = {value for key, value in dic.items() if value % 2 == 0}
    return new_dic

print("even value dictionary: ", even(dic))