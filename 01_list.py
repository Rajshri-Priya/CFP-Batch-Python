name = ["raj", "shri", "priya"]

# access item at index 0
print(name[0])  # raj
# access item at index 2
print(name[2])  # priya
# ---------------------------------------------------------
print("-------------by negative indexing-----------------")
# access items with negative index
print(name[-1])  # by which i print last element in list
# access item at index 2
print(name[-3])  # by which we access from last 3 element

# ------------slicing in Python-------------------------
print("------------------------------Slicing---------------------------------")
my_list = ['a', 'e', 'i', '0', 'u', 10, 20, 30, 40]
# items from index 2 to index 4
print(my_list[2:5])  # index[2]=i to index[5]=u
# items from index 5 to end
print(my_list[5:])
# items beginning to end
print(my_list[:])

# -----------------------------Add elements in list-----------------------------------------------
print("--------------Add element in list by append method--------------------")

numbers = [21, 34, 54, 12]
print("Before Append:", numbers)
# using append method
numbers.append(32)
print("After Append:", numbers)

# --------------------------------by extend()-------------------------------
print("----------------Add list by Extend method--------------------")
prime_numbers = [2, 3, 5]
print("List1:", prime_numbers)
even_numbers = [4, 6, 8]
print("List2:", even_numbers)
# join two lists
prime_numbers.extend(even_numbers)
print("List after append:", prime_numbers)
# ---------------------------by insert()---------------------

print("----------------Add element in list by INSERT method[with specific index]-------------------")

# a list of vowels
vowel = ['a', 'e', 'i', 'u']
# 'o' is inserted at index 3 (4th position)
vowel.insert(3, 'o')
print('List:', vowel)


# ------------------------count()------------------------
print("------count specific elements in list------")
# vowels list
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
# count element 'i'
count = vowels.count('i')
# print count
print('The count of i is:', count)
# count element 'p'
count = vowels.count('p')
# print count
print('The count of p is:', count)


# --------------------------deletion of elements in list-------------------
print("--------deletion of elements by del()[by indexes]-----")
prime = [1, 2, 3, 5, 7, 11, 13, 17, 19]
# deleting the second item
del prime[1]  # 2
print(prime)
# deleting the last item
del prime[-1]  # 19
print(prime)
# delete first two items
del prime[0: 2]  # [1,3]
print(prime)


print("--------deletion of elements by remove()[for specific element]-----")
# remove '13' from the list
prime.remove(13)
print(prime)

# -----------------------------deletion by pop()-------------------
print("-----------deletion by pop()[it return deleted element]------")
# languages list
languages = ['Python', 'Java', 'C++', 'Ruby', 'C']

# remove and return the last item
print('When index is not passed:')      # delete C
print('Return Value:', languages.pop())
print('Updated List:', languages)

# remove and return the last item
print('\nWhen -1 is passed:')           # delete ruby
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:')           # delete python
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)

# -----------------------------------------------------------------
