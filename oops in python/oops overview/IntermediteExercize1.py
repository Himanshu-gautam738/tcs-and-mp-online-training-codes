# function to find maximum element
def find_max(arr, size):
    max_value = arr[0]          # assume first element is max

    for i in range(1, size):
        if arr[i] > max_value:
            max_value = arr[i]

    return max_value

n = int(input("Enter size of array: "))

arr = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

result = find_max(arr, n)

print("Maximum element is:", result)