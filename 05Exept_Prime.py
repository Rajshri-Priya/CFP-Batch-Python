def check_if_prime(number):
    if number < 2:
        raise Exception("Number must be greater than 1")
    for i in range(2, number):
        if number % i == 0:
            raise Exception("Number is not prime")
    print("Number is prime")

try:
    check_if_prime(5)
    check_if_prime(3)
    check_if_prime(4)
except Exception as e:
    print(e)
