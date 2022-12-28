import math


# uc 3 ---line comparison with its length
# update --- include choices for line comparison(coordinate  or length)

def line_length(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def coordinate_equal(x1, y1, x2, y2, x3, y3, x4, y4):
    return x1 == x3 and y1 == y3 and x2 == x4 and y2 == y4


def are_lines_equal(length1, length2):
    return length1 == length2


def main():
    print("LINE COMPARISON")
    # User input for co-ordinates of two points
    points = []
    for i in range(4):
        x = int(input(f"Enter Co-ordinate for x{i + 1}: "))
        y = int(input(f"Enter Co-ordinate for y{i + 1}: "))
        points.append((x, y))
    # Ask the user which function to use to compare the lines
    method = input("Enter 'c' to compare using coordinate_equal or 'l' to compare using are_lines_equal: ")

    # Compare the lines using the chosen function
    if method == 'c':
        equal = coordinate_equal(points[0][0], points[0][1], points[1][0], points[1][1], points[2][0], points[2][1],
                                 points[3][0], points[3][1])
        if equal:
            print("The two lines are equal.")
        else:
            print("The two lines are not equal.")

    elif method == 'l':

        # Calculate the length of the first line
        length1 = line_length(points[0][0], points[0][1], points[1][0], points[1][1])
        print(f"Length of line1: {length1}")

        # Calculate the length of the second line
        length2 = line_length(points[2][0], points[2][1], points[3][0], points[3][1])
        print(f"Length of line2: {length2}")

        # Check equality of the two lines
        if are_lines_equal(length1, length2):
            print("The two lines are equal.")
        else:
            print("The two lines are not equal.")
    else:
        print("*** kindly enter choice from given option ***")


if __name__ == "__main__":
    main()
