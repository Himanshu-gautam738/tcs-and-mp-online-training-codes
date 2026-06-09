def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

strings = ["banana", "apple", "cherry", "date", "fig", "grape"]

print("Original list:", strings)

# Selection Sort
print("Selection Sort:", selection_sort(strings.copy()))

# Merge Sort
print("Merge Sort:", merge_sort(strings.copy()))

# Linear Search
target = "cherry"
print(f"Linear Search for '{target}': Index =", linear_search(strings, target))

# Binary Search (requires sorted list)
sorted_strings = merge_sort(strings.copy())
print("Sorted list for Binary Search:", sorted_strings)
print(f"Binary Search for '{target}': Index =", binary_search(sorted_strings, target))
