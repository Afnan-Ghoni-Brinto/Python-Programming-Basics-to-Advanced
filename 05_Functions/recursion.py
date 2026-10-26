def factorial(n):
    if n < 0:
        raise ValueError("Factorial requires a nonnegative integer")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

print("5! =", factorial(5))
countdown(3)
