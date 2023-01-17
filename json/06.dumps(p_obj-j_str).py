import json

data = {'name': 'Tanvi', 'age': 20, 'city': 'jammu'}
print(f"Before dumping into json , Type of object : {type(data)}")



# Dump the Python object to a JSON string, with separator and default
json_str = json.dumps(data, separators=(',', ':'), default=str)

# Print JSON string
print(f"After dumping into json, Type of object : {type(json_str)}")

print(json_str)
