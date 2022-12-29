# Write a Python program calculate the product, multiplying all the numbers of a given tuple.

def calculate_tuple_product(tup):
    product = 1
    # Iterate over the elements of the tuple
    for num in tup:
        # Multiply the current product by the current element
        product *= num
    return product


# Calculate the product for the first tuple
tup1 = (4, 3, 2, 2, -1, 18)
product1 = calculate_tuple_product(tup1)
print("Product of first tuple : ", product1)  # Output: -864

# Calculate the product for the second tuple
tup2 = (2, 4, 8, 8, 3, 2, 9)
product2 = calculate_tuple_product(tup2)
print("Product of second tuple : ", product2)  # Output: 27648
