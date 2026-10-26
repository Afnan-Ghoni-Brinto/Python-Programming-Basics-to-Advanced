square = lambda x: x*x
print(square(5))
numbers = [1, 2, 3, 4, 5]
print("Squares:", list(map(lambda n: n*n, numbers)))
print("Even:", list(filter(lambda n: n % 2 == 0, numbers)))
