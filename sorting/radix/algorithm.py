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
    while maxElement/exponent > 0:
        countingSort(arr,exponent)
        exponent *= 10

arr = [1,3,5,4,2,10,9,20,25,21]
print("Array before radix sort:", arr)
radixSort(arr)
print("Array after radix sort:", arr)
