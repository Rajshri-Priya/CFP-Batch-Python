# pallindrom strings
words = ["madam", "level", "word", "wow"]
palindrome_words = list(filter(lambda x: x== x[::-1], words))
print(palindrome_words) # Output: ["madam", "wow"]
