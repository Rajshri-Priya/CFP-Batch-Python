def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Division by zero!")
    except TypeError:
        print("Invalid types for division!")
    else:
        print("Result is", result)
    finally:
        print("Executing finally block")


divide(2, 1)
divide(2, 0)
divide(2, "a")

# --------------------------------------------------------------------------
print("***Exception by raise exception***")


def div(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


try:
    div(2, 0)
except ValueError as e:
    print(e)
