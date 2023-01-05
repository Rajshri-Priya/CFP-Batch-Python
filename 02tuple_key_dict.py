# Using tuple as a key in a dictionary

coordinates = [(4, 5), (6, 7), (8, 9)]
values = ['a', 'b', 'c']
coordinates_to_values = {coord: val for coord, val in zip(coordinates, values)}
print(coordinates_to_values)  # Output: {(4, 5): 'a', (6, 7): 'b', (8, 9): 'c'}
