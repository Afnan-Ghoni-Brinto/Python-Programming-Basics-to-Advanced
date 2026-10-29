class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("I am", self.name)

class Student(Person):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

    def show_department(self):
        print("Department:", self.department)

student = Student("Rahim", "CSE")
student.introduce()
student.show_department()
