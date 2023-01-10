# normal fxn
def starts_with_vowel(s):
    return s[0] in "aeiouAEIOU"


# lambda function to check if a string starts with a vowel
starts_with_vowel = lambda s: s[0] in "aeiouAEIOU"
print(starts_with_vowel("hello"))
print(starts_with_vowel("apple"))
