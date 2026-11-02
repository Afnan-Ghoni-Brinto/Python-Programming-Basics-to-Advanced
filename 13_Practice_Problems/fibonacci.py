terms = int(input("Number of terms: "))
if terms < 0:
    print("Enter a nonnegative number")
else:
    a, b = 0, 1
    for _ in range(terms):
        print(a, end=" ")
        a, b = b, a + b
    print()
