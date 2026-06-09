# Selection Sort
def selection_sort(prices):
    n = len(prices)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if prices[j] < prices[min_index]:
                min_index = j
        prices[i], prices[min_index] = prices[min_index], prices[i]
    return prices


# Merge Sort
def merge_sort(prices):
    if len(prices) > 1:
        mid = len(prices) // 2
        left_half = prices[:mid]
        right_half = prices[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                prices[k] = left_half[i]
                i += 1
            else:
                prices[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            prices[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            prices[k] = right_half[j]
            j += 1
            k += 1
    return prices


# Linear Search
def linear_search(prices, target):
    for index in range(len(prices)):
        if prices[index] == target:
            return index
    return -1


# Binary Search (requires sorted list)
def binary_search(prices, target):
    left, right = 0, len(prices) - 1
    while left <= right:
        mid = (left + right) // 2
        if prices[mid] == target:
            return mid
        elif prices[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

product_prices = [250, 100, 400, 150, 300, 200]

print("Original Prices:", product_prices)

# Selection Sort
print("Selection Sort:", selection_sort(product_prices.copy()))

# Merge Sort
print("Merge Sort:", merge_sort(product_prices.copy()))

# Linear Search
target_price = 300
print(f"Linear Search for {target_price}: Index =", linear_search(product_prices, target_price))

# Binary Search (requires sorted list)
sorted_prices = merge_sort(product_prices.copy())
print("Sorted Prices for Binary Search:", sorted_prices)
print(f"Binary Search for {target_price}: Index =", binary_search(sorted_prices, target_price))
