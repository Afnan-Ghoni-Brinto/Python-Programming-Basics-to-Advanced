class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

Student("Rahim", 20).show_info()
Student("Karim", 21).show_info()
