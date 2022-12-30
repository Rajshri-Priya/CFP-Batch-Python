# Write a function that takes in a list of integers and returns a dictionary where the keys are the integers, and the values are the number of times each integer appears in the list.

def count_occurrences(numbers):
    # create an empty dictionary to store the result
    result = {n: numbers.count(n) for n in numbers }
    # # iterate over the numbers in the input list
    # for n in numbers:
    #     # if the number is not already in the dictionary, add it as a key with a value of 1
    #     if n not in result:
    #         result[n] = 1
    #     # if the number is already in the dictionary, increment the value by 1
    #     else:
    #         result[n] += 1
    return result

# Example usage
numbers = [1, 2, 3, 1, 2, 3, 1, 2, 3]
counts = count_occurrences(numbers)
print(counts)  # {1: 3, 2: 3, 3: 3}