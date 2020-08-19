def binSearch(low,high,key,arr):
    while low<=high:
        mid = (high+low)//2
        if key<arr[mid]:
            high = mid-1
        elif key>arr[mid]:
            low = mid+1
        else:
            return mid
    return -1

n,q = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
#print(arr)
for _ in range(q):
    ans = binSearch(0,n-1,int(input()),arr)
    print("NO") if ans==-1 else print("YES")
