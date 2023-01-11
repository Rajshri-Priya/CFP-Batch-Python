# largest no
from functools import reduce
numbers = [3, 4, 5, 6, 2, 1]
largest = reduce(lambda x, y: x if x > y else y, numbers)
print(largest)  # Output: 6
