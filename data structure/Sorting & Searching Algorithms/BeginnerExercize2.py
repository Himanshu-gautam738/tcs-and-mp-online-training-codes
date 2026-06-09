arr=[4,2,7,1,9]
def linearsearch(arr,target):
     n=len(arr)
     for i in range(0,n):
         if target==arr[i]:
              return i
     return -1

x=linearsearch(arr,7)
print(x)
