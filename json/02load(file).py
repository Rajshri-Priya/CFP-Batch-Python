import json

# Open JSON file 
with open('employees.json', 'r') as f:
    # Load the JSON data from the file into a Python object
    employees = json.load(f)

# Set salary 
ch_salary = 50000

for employee in employees:
    # Check if the employee's salary is above the given salary
    if employee['salary'] > ch_salary:
        # Print employee's name
        print(employee['name'])
    else:
        print(f"{employee['name']}'s salary is less than {ch_salary}")
