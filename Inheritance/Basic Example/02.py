class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_name(self):
        return self.name

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    
    def get_student_id(self):
        return self.student_id

person = Person("raj", 30)
student = Student("Shri", 20, "123")

print(person.get_name())
print(student.get_name())
print(student.get_student_id())
