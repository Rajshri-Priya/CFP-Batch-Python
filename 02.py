try:
    int("hello")
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# -------------------------------------
try:
    numbers = [1, 2, 3]
    print(numbers[3])
except IndexError:
    print("Index out of range! Please enter a valid index.")

#--------------------------------------
