# common prefix
from functools import reduce
words = ["hello", "help", "helium"]
common_prefix = reduce(lambda x, y: x if y.startswith(x) else y[:len(x)], words)
print(common_prefix) # Output: "hel"
