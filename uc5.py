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
# --------------------------------------------------------------------------------------------------
# uc2-uc3 -- calculate wage for full and half day
def calculate_wage():
    wage_per_hr = 20
    totalsalary = 0
    emp_hr = 0
    # uc5---for one month having 20 working days
    for i in range(21):
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
        else:
            print(attendence)
        salary = (emp_hr * wage_per_hr)
        print("Employe salary :", salary)
        totalsalary += salary  # for calculating total salary of 20 days
    print("Total Salary of month: ", totalsalary)
calculate_wage()
