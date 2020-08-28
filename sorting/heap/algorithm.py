import heapq
def heapSort(arr):
    tempArr = []
    heapq.heapify(arr)
    while arr:
        tempArr.append(heapq.heappop(arr))
    return tempArr

arr = [5,2,-1,0,1,6,9]
print("Array before heap sort:", arr)
print("Array after heap sort:", heapSort(arr))
