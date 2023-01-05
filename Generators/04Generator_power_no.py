# Generating the powers of a number
def powers_of_x(x):
    n = 1
    while True:
        yield x**n
        n += 1

powers_of_2 = powers_of_x(3)

for i in range(5):
    print(next(powers_of_2))
