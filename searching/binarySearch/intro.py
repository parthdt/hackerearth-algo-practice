def binSearch(low,high,rank,arr):
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<rank:
            low = mid+1
        elif arr[mid]>rank:
            high = mid-1
        else:
            return mid+1
    return -1

size = int(input())
arr = list(map(int,input().split()))
arr.sort()
queries = int(input())
for _ in range(queries):
    query = int(input())
    print(binSearch(0,size,query,arr))
