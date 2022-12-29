#  Write a Python program to replace last value of tuples in a list.
list1 = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
list2 = []
for i in list1:
    list2.append(i[:-1] + (100,))
print(list2)
