def generate_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b

for num in generate_fibonacci(5):
    print(num)

# Output: 0 1 1 2 3
