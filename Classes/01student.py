class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

student = Student("Raj", 22, [90, 95, 100])
print(f"Average grade: {student.get_average_grade()}")
