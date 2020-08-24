n, x = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(x):
    min = i
    for j in range(i+1,n):
        if arr[j]<arr[min]:
            min = j
    arr[i], arr[min] = arr[min], arr[i]
print(*arr)
