arr=[5,3,8,4,2]
def bubblesort(arr):
    num=len(arr)
    for i in range(num-2,-1,-1):
        for j in range(0,i+1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
x=bubblesort(arr)
print(x)