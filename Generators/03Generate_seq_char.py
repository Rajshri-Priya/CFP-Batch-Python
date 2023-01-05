# generate sequence of character

def generate_characters(string):
    for char in string:
        yield char

for char in generate_characters("Hello"):
    print(char)

# Output: H e l l o
