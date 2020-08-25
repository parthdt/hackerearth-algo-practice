def insertionSort(arr):
    for i in range(len(arr)):
        temp = arr[i]
        j = i
        while j>0 and temp<arr[j-1]:
            arr[j]=arr[j-1]
            j-=1
        arr[j]=temp
    return arr


n = int(input())
arr = list(map(int,input().split()))

evens = [item for item in arr if item%2==0]
odds = [item for item in arr if item%2!=0]
evens = insertionSort(evens)
odds = insertionSort(odds)
evens.append(sum(evens))
evens.extend(odds)
evens.append(sum(odds))
print(evens)
