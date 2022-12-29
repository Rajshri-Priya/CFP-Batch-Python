# question----- generator and generator comprehension----# ()
# ------------------------List Comprehension---[]----------------
# shorter syntax when you want to create a new list based on the values of an existing list.
# ek line main list make krne ka way

# ls=[]
# for i in range(30):
#     if i % 3 == 0:
#         ls.append(i)

# syntax=[expression for item in iterable if condition == True] ## if condition optional
# [i for i in range(30)] ---i[expression] or what i want to take , i[item],range()[iterable]

print("--------------List Comprehension---[]----------------")
ls = [i for i in range(30) if i % 3 == 0]  # it print no.from(0-29)
print(ls)


# Example1: What is the list comprehension to generate a list of the first 10 squares?
print("--list of the first 10 squares--")
squares = [x*x for x in range(10)]
print(squares)


# Example2: What is the list comprehension to generate a list of even numbers between 0 and 20?
print("--list of even numbers between (0-20)--")
even = [x for x in range(20) if x % 2 == 0]
print(even)


# Example3: What is the list comprehension to generate a list of the first letters of each word in the given list?
print("--generate a list of the first letters of each word in the given list--")
list1 = ["apple", "banana", "cherry"]
first_letter = [word[0] for word in list1]
print(first_letter)


# Example4: What is the list comprehension to generate a list of all possible products of two numbers between 0 and 2?
print("---generate a list of all possible products of two numbers between (0-2)---")
products = []
for i in range(3):          # i=0        i=1        i=2
    for j in range(3):      # j=0,1,2    j=0,1,2    j=0,1,2
        products.append(i*j)    # (0,0,0)(0,1,2)(0,2,4)
print(products)
print("***********************************************")
product = [x*y for x in range(3) for y in range(3)]  # there we can use nested for loop
print(product)


# Example5: What is the list comprehension to generate a list of all words from the given list in uppercase?
print("---generate a list of all words from the given list in uppercase---")
list1 = ["apple", "banana", "cherry"]
word_upper = [word.upper() for word in list1]
print(word_upper)


# -----------------dict comprehension---{key:value}---------
# dict1 = { 0:"item 1",1:"item 2" ......... ,99:"item 100"}

print("-----------------dict comprehension---{key:value}---------")
dict1 = {i: f"item {i}" for i in range(100)}
print("dict [0-99] : ", dict1)

"""advantage ---create big dictionaries
             ---reverse dictionary"""


# make new dict and stored it in dict1
dict1 = {i: f"item {i}" for i in range(5)}
print("dict[0-5] : ", dict1)
# i want to rewrite dict2 in the form of value key
dict2 = {value: key for key, value in dict1.items()}
print(dict1, "\n", dict2)



# -------------------SET Comprehension----------------
print("-------------------SET Comprehension----------------")
vowels = {x for x in ["a", "e", "i", "o", "u", "a", "e", "i", "o"]}
print("vowels are: ", vowels)
print(type(vowels))

