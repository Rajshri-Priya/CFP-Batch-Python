# ------uc2: calculate employee wage--------

# uc1: check employee is present or absent

def check_presence():
    random_num = random.randint(0, 1)
    print(random_num)
    if random_num == 1:
        return "Present"
    else:
        return 'Absent'
# print(check_presence())

# uc2: calculate employee wage for fullday
def calculate_wage():
    wage_per_hr = 20
    full_day_hour = 8
    present = check_presence()
    if present == 'Present':
        salary = (full_day_hour * wage_per_hr)
        print("Employe salary :", salary)
calculate_wage()