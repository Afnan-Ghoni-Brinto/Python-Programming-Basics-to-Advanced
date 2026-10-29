def squares(limit):
    for number in range(limit):
        yield number ** 2

for value in squares(5):
    print(value)
