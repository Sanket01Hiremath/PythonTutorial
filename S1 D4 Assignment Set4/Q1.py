
def bubbleSort(arr,n):
    for i in range(0,n-1):
        for j in range(0,n-1):
            if arr[j+1]>arr[j]:
                arr[j+1],arr[j]=arr[j],arr[j+1]
    print(arr)


arr=[5,4,3,7,3,1,2]
n=len(arr)
bubbleSort(arr,n)
