def countingSort(arr,exponent):
    n = len(arr)
    output = [0]*n
    count = [0]*10

    for i in range(n):
        index = arr[i]/exponent
        count[int(index%10)]+=1

    for i in range(1,10):
        count[i] += count[i-1]

    i = n-1
    while i>= 0:
        index = arr[i]/exponent
        output[ count[int(index%10)] - 1] = arr[i]
        count[int(index%10)]-=1
        i-=1

    i = 0
    for i in range(n):
        arr[i]=output[i]

def radixSort(arr):
    maxElement = max(arr)
    exponent = 1
    while int(maxElement) > 0:
        countingSort(arr,exponent)
        print(*arr)
        exponent = exponent*10
        maxElement=maxElement/exponent
    countingSort(arr,exponent)
    print(*arr)

n = int(input())
arr = list(map(int,input().split()))
radixSort(arr)

