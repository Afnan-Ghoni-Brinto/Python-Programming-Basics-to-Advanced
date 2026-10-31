def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index
    return -1

print(linear_search([10, 20, 30, 40], 30))  # 2
# Time complexity: O(n); extra space: O(1).
