# Write a function that takes in a dictionary and returns a new dictionary containing only the key-value pairs where the value is a prime number.
import math
def get_prime_values(d):
    # prime fxn
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    # use a dictionary comprehension to create a new dictionary containing only the key-value pairs where the value is a prime number
    result = {k: v for k, v in d.items() if is_prime(v)}
    return result

d = {"a": 2, "b": 3, "c": 4, "d": 5, "e": 6}
primes = get_prime_values(d)
print(primes)  # {"b": 3, "d": 5}