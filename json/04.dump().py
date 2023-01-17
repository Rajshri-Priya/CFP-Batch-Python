import json

# Python object to be dumped
data = {'dump()': '''convert a Python object to a JSON string and write it to a file.\
    It will overwrite the existing content if file already exists with the same name.'''}

# Open a file in write mode
with open('dump.json', 'w') as f:
    # Dump the Python object to the file
    json.dump(data, f)
    