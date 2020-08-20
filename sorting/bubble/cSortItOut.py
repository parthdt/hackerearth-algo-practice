n = int(input())
arr = [(int(j),i) for i,j in enumerate(map(int,input().split()))]
arr.sort()
print(*(i for j,i in arr))
