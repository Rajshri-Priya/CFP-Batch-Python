# uc1 --take input from user for coordinates and calculate length of line
import math


def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():

    print("LINE COMPARISON")
    # User input for co-ordinates of two points
    x1 = int(input("Enter Co-ordinate for x1: "))
    y1 = int(input("Enter Co-ordinate for y1: "))
    x2 = int(input("Enter Co-ordinate for x2: "))
    y2 = int(input("Enter Co-ordinate for y2: "))

    # Function call and print the length of a line
    print("Length of a Line is", line_length(x1, y1, x2, y2))


if __name__ == "__main__":
    main()
