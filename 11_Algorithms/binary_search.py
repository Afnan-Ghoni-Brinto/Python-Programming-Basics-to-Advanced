def binary_search(numbers, target):
    """numbers must be sorted in ascending order."""
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return mid
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([10, 20, 30, 40, 50], 40))  # 3
# Time complexity: O(log n); extra space: O(1).
