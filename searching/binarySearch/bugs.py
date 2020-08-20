def binSearch(low,high,key,arr):
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<key:
            low=mid+1
        elif arr[mid]>key:
            high=mid-1
        else:
            return mid
    return -1

n = int(input())
arr = []
count = 0
for _ in range(n):
    a = list(map(int,input().split()))
    if a[0]==1:
        if count==0:
            arr.insert(a[1],1)
            count=1
        elif count==1:
            arr.append(a[1])
            a.sort()
            count=2
        else:
            index = binSearch(0,count-1,a[1],arr)
            if index>=count:
                a.insert(a[1],count)
            elif index<0:
                a.insert(a[1],0)
            else:
                a.insert(a[1],index)
            count+=1
            print(index,arr)
    else:
        if count>2:
            print(arr[-(count//3)])
        else:
            print("Not enough enemies")

