# Array operations
arr = [10, 20, 30, 40]

# 1. Insertion (append at end)
arr.append(50)         # [10, 20, 30, 40, 50]

# 2. Access by index - O(1)
print("Element at index 2:", arr[2])  # 30

# 3. Deletion by index
arr.pop(1)             # Removes 20 -> [10, 30, 40, 50]

# 4. Traversal
print("Array elements:")
for item in arr:
    print(item, end=" ")
print()