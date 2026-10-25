numbers = list(range(1, 11))
squares = [n*n for n in numbers]
evens = [n for n in numbers if n % 2 == 0]
labels = ["even" if n % 2 == 0 else "odd" for n in numbers]
print(squares)
print(evens)
print(labels)
print({n: n*n for n in range(1, 4)})
