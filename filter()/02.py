# get all strings with more than 3 characters
words = ["cat", "dog", "elephant", "bird"]
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words) # Output: ["elephant", "bird"]
