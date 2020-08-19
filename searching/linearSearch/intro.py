n,i = map(int,input().split())

arr = list(map(int,input().split()))
finalIndex = -1

for index in range(n):
    if arr[index] == i:
        finalIndex = index
print(finalIndex+1)     #They wanted final index of occurence of i, but it started from 1 not 0, hence the +1

