def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Index found
    return -1         # Not found

print(linear_search([5, 2, 9, 1, 7], 9))  # Output: 2