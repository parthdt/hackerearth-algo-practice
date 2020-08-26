def partition(arr,start,end):
    i = start + 1
    pivot = arr[start]

    for j in range(start+1,end+1):
        if arr[j]<pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
    arr[start], arr[i-1] = arr[i-1], arr[start]
    return i-1

def quickSort(arr,start,end):
    if start<end:
        pivot = partition(arr,start,end)
        quickSort(arr,start,pivot-1)
        quickSort(arr,pivot+1,end)

t = int(input())
for _ in range(t):
    m,n = map(int,input().split())
    if m>n:
        print("NO")
    else:
        boys = list(map(int,input().split()))
        girls = list(map(int,input().split()))
        quickSort(boys,0,m-1)
        quickSort(girls,0,n-1)
        flag = 0
        for index in range(m):
            if boys[index]<=girls[index]:
                print("NO")
                flag = 1
                break
        if flag!=1:
            print("YES")


        
