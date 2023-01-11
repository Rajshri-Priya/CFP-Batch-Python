# filter string start with "e"
words = ["cat", "dog", "elephant", "bird"]
words_starts_with_e = list(filter(lambda x: x.startswith("e"), words))
print(words_starts_with_e) # Output: ["elephant"]
