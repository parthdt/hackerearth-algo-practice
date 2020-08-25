def insertionSort(arr,size):
    for i in range(size):
        temp = arr[i]
        j=i
        while j>0 and temp<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=temp
    return arr

n = int(input())
arr = list(map(int,input().split()))
tempArr = [item for item in arr]
tempArr = insertionSort(tempArr,n)
finalArr = [tempArr.index(item)+1 for item in arr]
print(*finalArr)


