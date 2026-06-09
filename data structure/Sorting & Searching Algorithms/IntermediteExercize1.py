arr=[1,3,5,7,8,9]
def printbinarysearch(arr,target):
    n=len(arr)
    low=0
    heigh=n-1
    while low<heigh:
        mid=(low+heigh)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            heigh=mid-1

x=printbinarysearch(arr,8)
print("target is :",x)
        