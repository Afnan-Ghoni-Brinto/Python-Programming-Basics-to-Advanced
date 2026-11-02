number = int(input("Enter a nonnegative integer: "))
if number < 0:
    print("Factorial is undefined for negative integers")
else:
    result = 1
    for i in range(2, number + 1):
        result *= i
    print("Factorial:", result)
