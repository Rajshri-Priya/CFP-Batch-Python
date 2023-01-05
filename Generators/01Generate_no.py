def generate_numbers(n):
    for i in range(n):
        yield i

for num in generate_numbers(5):
    print(num)

# Output: 0 1 2 3 4
