n = int(input())
arr = list(map(int,input().split()))

swaps = 0

for i in range(n-1):
    for j in range(n-1-i):
        if(arr[j]>arr[j+1]):
            swaps+=1
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(swaps)
