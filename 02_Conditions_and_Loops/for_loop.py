for number in range(1, 6):
    print(number, "squared =", number ** 2)
print("Even numbers:")
for number in range(2, 11, 2):
    print(number, end=" ")
print("\nMultiplication table:")
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end=" ")
    print()
