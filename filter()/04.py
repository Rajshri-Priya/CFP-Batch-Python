# filter positive number
numbers = [-5, -4, 0, 1, 2, 3, 4, 5]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)  # Output: [1, 2,3,4,5]
