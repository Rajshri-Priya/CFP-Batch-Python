import json

# Open the JSON file 
with open('products.json', 'r') as f:
    # Load the JSON data from the file into a Python object # {decode the data}
    products = json.load(f)

# variable to store the total cost
total_cost = 0

for product in products:
    # Add  price of the current product to the total cost
    total_cost += product['price']

# Total cost
print(f'Total cost of all products: {total_cost}')
