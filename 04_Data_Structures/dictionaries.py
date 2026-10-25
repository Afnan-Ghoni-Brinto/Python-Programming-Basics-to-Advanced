student = {"name": "Rahim", "age": 20, "department": "CSE"}
print(student["name"])
print(student.get("cgpa", "Not available"))
student["cgpa"] = 3.8
for key, value in student.items():
    print(f"{key}: {value}")
student.pop("age")
print(student)
