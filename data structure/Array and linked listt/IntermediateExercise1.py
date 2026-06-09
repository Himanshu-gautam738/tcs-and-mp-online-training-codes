arr = [1, 5, 7, -1, 5]
target = 6
pairs = []
n = len(arr)
for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))

print(pairs)
