# --------------basic way to open and close file---------
# a = open('file.txt')
# for each in a:
#     print (each)
# a.close()

# -------------------Read / Write-------------------------
print("-------------------Read / Write-------------------------")
with open('new_file.txt', 'w') as f:
    f.write('This is a new file.')
with open("new_file.txt", 'r') as  f:
     print(f.read())
    

# --------------------Appending----------------------------

print("-------------------Append And Read-------------------------")

with open('new_file.txt', 'a') as f:
    f.write('This is a new line appended to the file.')
with open("new_file.txt", 'r') as  f:
    print(f.read())
    # print(f.readline())


# ------------tell(),readline(),seek(),split()-----------------------

print("------------tell(),readline(),seek(),split()-----------------------")

with open("file.txt", 'r') as  file:
    # contents = file.read()
    # print(contents)
    print(file.tell())      # tell position of ptr
    print(file.readline())  # read line by line
    print(file.seek(50))    # take specific argument by which show output
    print(file.readline())

    for line in file:
        print(line.split())     # convert line of file in  list and splited by ","
        print(file.readline())

# -------------Copying 1 file data to another----------------------------

with open('abc.txt', 'r') as f1:
    with open('math.txt', 'w') as f2:
        f2.write(f1.read())
        
with open('abc.txt', 'r') as f1:
    print(f1.read())

with open('math.txt', 'r') as f2:
    print(f2.read())
