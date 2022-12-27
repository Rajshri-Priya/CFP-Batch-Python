# identity operator
# is	True if the operands are identical (refer to the same object)
# is not	True if the operands are not identical (do not refer to the same object)
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1, 2, 3]
y3 = [1, 2, 3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False
