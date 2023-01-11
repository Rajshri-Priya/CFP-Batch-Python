# filter vowel character 
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
vowels = list(filter(lambda x: x in ['a','e','i','o','u'], chars))
print(vowels) # Output: ['a', 'e']
