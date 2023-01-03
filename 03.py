try:
    student_grades = {"Alice": 90, "Bob": 80}
    print(student_grades["Charlie"])
except KeyError:
    print("Key not found! Please make sure the key exists in the dictionary.")
