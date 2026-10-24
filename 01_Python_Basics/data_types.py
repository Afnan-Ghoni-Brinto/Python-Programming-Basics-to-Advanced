examples = [42, 3.14, 2+3j, "Python", True, None,
            [1, 2], (1, 2), {1, 2}, {"name": "Rahim"}]
for item in examples:
    print(repr(item), "->", type(item).__name__)
