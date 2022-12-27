# program to display numbers from 1 to 5
# initialize the variable
i = 1
n = 5

# while loop from i = 1 to 5
while i <= n:
    print(i)
    i += 1


print("*******************************")
print(" to find first 5 multiples of 6")

i = 1

while i <= 10:
    print('6 * ', i, '=', 6 * i)
    if i >= 5:
        break
    i = i + 1
