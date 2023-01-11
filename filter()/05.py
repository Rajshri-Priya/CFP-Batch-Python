# remove duplicate value
numbers = [1, 1, 2, 3, 3, 4, 4, 5, 5]
unique_numbers = list(set(filter(lambda x: True, numbers)))
print(unique_numbers) # Output: [1, 2, 3, 4, 5]
