# concatenation of string

from functools import reduce
words = ["hello", "world"]
concatenated = reduce(lambda x, y: x+y, words)
print(concatenated) # Output: "helloworld"
