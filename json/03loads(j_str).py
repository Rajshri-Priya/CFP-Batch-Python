import json

# JSON string to be parsed
json_str = '{"name": "raj", "age": 22, "address":"Jammu & Kashmir"}'

# Parse the JSON string and convert it to a Python object 
data = json.loads(json_str)

# Access the properties of the object
# print(type(data["name"]))  
# print(data["age"])   

for key, value in data.items():
    print(f"{key}: {value}")
