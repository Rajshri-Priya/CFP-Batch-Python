# Write a Python program to compute element-wise sum of given tuples.
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 5, 2, 1)
tuple3 = (2, 2, 3, 1)
# map return object which save in tuple or we can convert it in list also
result = tuple(map(sum, zip(tuple1, tuple2, tuple3)))  # map(fun, iter)

print(result)
