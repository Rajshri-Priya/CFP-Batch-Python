import math
# uc2--- compare two lines by its coordinates
# def line_length(x1, y1, x2, y2):
#     return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# def is_equal(x1, y1, x2, y2, x3, y3, x4, y4):
#     return line_length(x1, y1, x2, y2) == line_length(x3, y3, x4, y4)

def coordinate_equal(x1, y1, x2, y2, x3, y3, x4, y4):
    return x1 == x3 and y1 == y3 and x2 == x4 and y2 == y4


def main():
    # User input for co-ordinates of two points
    # x1 = int(input("Enter Co-ordinate for x1: "))
    # y1 = int(input("Enter Co-ordinate for y1: "))
    # x2 = int(input("Enter Co-ordinate for x2: "))
    # y2 = int(input("Enter Co-ordinate for y2: "))

    # Function call and print the length of a line
    # print("Length of a Line is", line_length(x1, y1, x2, y2))

    # User input for co-ordinates of two points
    # x3 = int(input("Enter Co-ordinate for x3: "))
    # y3 = int(input("Enter Co-ordinate for y3: "))
    # x4 = int(input("Enter Co-ordinate for x4: "))
    # y4 = int(input("Enter Co-ordinate for y4: "))

    # print("Length of a Line is", line_length(x3, y3, x4, y4))
    #  -------------------------------------------------------------------------------------------------------
    print("LINE COMPARISON")
    # User input for co-ordinates of two points by using list
    points = []
    for i in range(4):
        x = int(input(f"Enter Co-ordinate for x{i + 1}: "))
        y = int(input(f"Enter Co-ordinate for y{i + 1}: "))
        points.append((x, y))
    # Function call and print the equality of two lines
    print("Are the two lines equal?", coordinate_equal(points[0][0], points[0][1], points[1][0], points[1][1],points[2][0], points[2][1], points[3][0], points[3][1]))


if __name__ == "__main__":
    main()
