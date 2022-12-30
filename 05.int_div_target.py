# Write a function that takes in a list of integers and returns a new list containing only the integers that are divisible by a target value.

def divisible_by(numbers, target):
    # use a list comprehension to create a new list of integers that are divisible by the target value
    result = [n for n in numbers if n % target == 0]
    return result


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 2
divisibles = divisible_by(numbers, target)
print(divisibles)  # [2, 4, 6, 8, 10]
