def modifiedCountingSort(arr):
    
    maxElement = max(arr)
    countArr = [0]*(maxElement+1)

    for element in arr:
        countArr[element]+=1

    sortedArr = []

    for index in range(maxElement+1):
        count = countArr[index]
        if count!=0:
            print(index,count)

n = int(input())
modifiedCountingSort(list(map(int,input().split())))


