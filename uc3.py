import random
# uc1: check employee is present or absent

def check_presence():
    random_num = random.randint(0, 1)
    print(random_num)
    if random_num == 1:
        return "Present"
    else:
        return 'Absent'
# print(check_presence())


def calculate_wage():
    wage_per_hr = 20
    attendence = check_presence()
    if attendence == 'Present':
        print("Employee is Present")
        rand = random.randint(1, 2)
        if rand == 1:
            print("present for full day")
            emp_hr = 8
        else:
            print("present for half day")
            emp_hr = 4
        salary = (emp_hr * wage_per_hr)
        print("Employe salary :", salary)
    else:
        print(attendence)
calculate_wage()