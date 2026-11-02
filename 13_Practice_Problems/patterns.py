rows = 5
print("Star triangle:")
for i in range(1, rows + 1):
    print("* " * i)
print("Number triangle:")
for i in range(1, rows + 1):
    print(" ".join(str(n) for n in range(1, i + 1)))
