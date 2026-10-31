def selection_sort(numbers):
    result = numbers.copy()
    for i in range(len(result)):
        minimum = i
        for j in range(i + 1, len(result)):
            if result[j] < result[minimum]:
                minimum = j
        result[i], result[minimum] = result[minimum], result[i]
    return result

def insertion_sort(numbers):
    result = numbers.copy()
    for i in range(1, len(result)):
        value = result[i]
        j = i - 1
        while j >= 0 and result[j] > value:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = value
    return result

numbers = [9, 3, 7, 1, 5]
print("Selection:", selection_sort(numbers))
print("Insertion:", insertion_sort(numbers))
print("Built-in:", sorted(numbers))
