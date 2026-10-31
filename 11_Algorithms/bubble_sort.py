def bubble_sort(numbers):
    result = numbers.copy()
    for i in range(len(result)):
        swapped = False
        for j in range(len(result) - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break
    return result

print(bubble_sort([5, 1, 4, 2, 8]))
# Worst-case time: O(n^2); extra space: O(n) for the copy.
