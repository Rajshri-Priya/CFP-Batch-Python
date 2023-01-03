
def check_for_negatives(numbers):
    for number in numbers:
        if number < 0:
            raise Exception("Negative numbers are not allowed")


# check_for_negatives(numbers):
try:
    check_for_negatives([1, 2, -3])
except Exception as e:
    print(e)

# check_for_negatives([1, 2, 3]) # okay
# check_for_negatives([1, 2, -3])  # raises exception
