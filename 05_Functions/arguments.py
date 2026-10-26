def greet(name="Guest"):
    print("Hello", name)

def total(*numbers):
    return sum(numbers)

def show_student(**details):
    for key, value in details.items():
        print(key, value)

greet()
greet(name="Rahim")
print("Total:", total(10, 20, 30))
show_student(name="Rahim", department="CSE")
