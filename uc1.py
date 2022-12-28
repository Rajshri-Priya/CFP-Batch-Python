import random
# uc1: check employee is present or absent
# use random fxn

def check_presence():
    random_num = random.randint(0, 1)
    print(random_num)
    if random_num == 1:
        return "Present"
    else:
        return 'Absent'
print(check_presence())
