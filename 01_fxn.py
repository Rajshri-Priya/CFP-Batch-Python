def main():
    options = {
        1: factor,
        2: factorial,
        3: reverse,
        4: prime,
        5: fibonacci,
        6: palindrome,
        7: hormonic,
        8: power,
        9: leapyear

    }

    while True:
        print()
        print("CHOOSE OPTIONS")
        print(" 1.FACTOR \n 2.FACTORIAL\n 3.REVERSE\n 4.PRIME \n 5.FIBONACCI \n 6.PALINDROME \n 7.HORMONIC \n 8.POWER \n 9.LEAP YEAR \n 10.EXIT\n")

        n = int(input("Your selected option : "))

        if n == 10:
            break
        elif n in options:
            options[n]()
        else:
            print("PLEASE WRITE VALID OPTION IN BETWEEN (1-9)")


# code for factor
def factor():
    n = int(input("Enter the Number:"))  # taking input from user
    print("Factors:")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


def factorial():

    fact = 1
    num = int(input("Enter any Number: "))
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial of", num, "is:", fact)


def reverse():

    num = int(input("Enter a Number to reverse"))
    num_reverse = 0
    while num > 0:
        remainder = num % 10
        num_reverse = (num_reverse * 10) + remainder
        num = num // 10
    print("Reverse No. is", num_reverse)


def prime():

    num = int(input("Enter the Number"))
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(num, "is Not Prime Number")
            return
    print(num, "is Prime Number")


def fibonacci():

    n1 = 0
    n2 = 1
    number = int(input("Enter the number of elements: "))
    print(n1, n2, end=" ")
    for i in range(2, number):
        n3 = n1 + n2
        print(n3, end=" ")
        n1 = n2
        n2 = n3


def palindrome():

    rev = 0
    n = int(input("Enter the Number: "))
    temp = n
    while n > 0:
        r = n % 10
        rev = (rev * 10) + r
        n = n // 10
    if temp == rev:
        print("Number is Palindrome.")
    else:
        print("Number is not Palindrome")


def hormonic():

    print("Hormonic series like 1/1+1/2+1/3+1/4+....1/n")
    print("enter the number : ")
    n = int(input())
    for i in range(1, n + 1):
        print("1/{0} + ".format(i), end="")


def power():

    print("FOR CALCULATING POWER OF 2")
    print("ENTER POWER FOR (2^n): ")
    num = int(input())
    power = 1
    for i in range(1, num + 1):
        power = (2 * power)
        print(power)


def leapyear():

    print("ENTER YEAR FOR CHECKING:")
    year = int(input())

    if 999 < year < 10000:  # year > 999 and year < 10000
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print(f"{year} is leap year")
        else:
            print(f"{year} is not leap year")
    else:
        print("please write 4 digit year")


main()
