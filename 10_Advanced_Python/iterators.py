values = [10, 20, 30]
iterator = iter(values)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
