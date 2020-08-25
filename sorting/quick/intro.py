def partition(arr,start,end):
    i = start + 1
    pivot = arr[start]

    for j in range(start+1,end+1):
        if arr[j]<pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return i-1

def quickSort(arr, start, end):
    if start<end:
        pivot = partition(arr, start, end)
        quickSort(arr,start,pivot-1)
        quickSort(arr,pivot+1,end)

size = int(input())
array = list(map(int,input().split()))
quickSort(array,0,size-1)
print(*array)

