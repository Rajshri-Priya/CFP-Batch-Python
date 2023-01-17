import json

# Python object to be dumped
data = {'Syntax': 'data, file, indent, sort_keys', 'data': 'which gona dumped in file', 'file': 'file_nameby which json created',\
    'indent':'specify the num. of spaces to use for indentation', 'sort_keys':'sort the keys in alphabetical order'}

# Open a file in write mode
with open('dump(syntax).json', 'w') as f:
    # Dump the Python object to the file, with indentation and sorting keys
    json.dump(data, f, indent=4, sort_keys=True)
