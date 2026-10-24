name = input("Enter your name: ")
try:
    age = int(input("Enter your age: "))
    print(f"Hello {name}! Next year you will be {age + 1}.")
except ValueError:
    print("Age must be a whole number.")
print("A", "B", "C", sep=" - ", end="!\n")
