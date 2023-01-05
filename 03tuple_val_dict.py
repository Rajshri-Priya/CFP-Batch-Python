# Using tuple as a value in a dictionary


names = ['Raj', 'Shri']
values = [('NYC', 'USA'), ('SF', 'USA')]
name_to_location = {name: value for name, value in zip(names, values)}
print(name_to_location)  
