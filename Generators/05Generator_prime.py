# prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
        return True

def prime_generator(max_number):
    n = 2
    while n <= max_number:
        if is_prime(n):
            yield n
        n += 1

max_number = int(input("Enter the maximum number: "))
for i in prime_generator(max_number):
    print(i)