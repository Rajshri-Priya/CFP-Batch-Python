# string pallindrome in list by using indexing
def palindrome_strings(strings):
    palindromes = [s for s in strings if s == s[::-1]]  # [Start : stop : stepcount]
    # for s in strings:
    #     if s == s[::-1]:  # check if the string is the same forwards and backwards
    #         palindromes.append(s)
    return palindromes


strings = ["racecar", "hello", "level", "pivot", "redder"]
palindromes = palindrome_strings(strings)
print(palindromes)  # ['racecar', 'level', 'redder']