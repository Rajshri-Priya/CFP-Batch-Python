# try:
#     # code that may cause exception
# except:
#     # code to run when exception occurs


# Denominator cannot be 0
try:
    numerator = 10
    denominator = 0

    result = numerator / denominator
    print(result)

except:
    print("Error: Denominator cannot be 0.")

# try...finally
# finally: This block is always executed no matter whether there is an exception or not.
finally:
    print("This is finally block.")



#--------------------------------------------------------------------------------------
# Catching Specific Exceptions 
try:
    even_numbers = [2, 4, 6, 8]
    print(even_numbers[5])

except ZeroDivisionError:
    print("Denominator cannot be 0.")

except IndexError:
    print("Index Out of Bound.")

# try with else clause

# program to print the reciprocal of even numbers
try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0  # The assert keyword lets you test if a condition in your code returns True, if not, the program will raise an AssertionError
except:
    print("Not an even number!")
else:
    reciprocal = 1 / num
    print(f"Receprocal of {num} is: ", reciprocal)





