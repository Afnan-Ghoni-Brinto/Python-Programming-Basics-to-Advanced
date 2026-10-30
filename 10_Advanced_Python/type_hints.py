def add(a: int, b: int) -> int:
    return a + b

def average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Numbers cannot be empty")
    return sum(numbers) / len(numbers)

print(add(2, 3))
print(average([3.0, 4.0, 5.0]))
//Done
