def double_and_add_one(x):
    return 2*x + 1

numbers = [1, 2, 3, 4]
doubled_and_incremented = list(map(double_and_add_one, numbers))
print(doubled_and_incremented) # Output: [3, 5, 7, 9]
