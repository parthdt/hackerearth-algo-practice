def countingSort(arr):
    maxElement = max(arr)
    countArr = [0]*(maxElement+1)

    for element in arr:
        countArr[element]+=1

    sortedArr = []
    for index in range(maxElement+1):
        count = countArr[index]
        while count:
            sortedArr.append(index)
            count-=1
    return sortedArr

arr = [5,4,2,1,3]
print("Array before and after counting sort:", arr, countingSort(arr))


