n,m = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))
sumArr = [[0]*m for _ in range(n)]
sumArr[0][0] = arr[0][0]
for i in range(1,n):
    sumArr[i][0] = sumArr[i-1][0] + arr[i][0]
for j in range(1,m):
    sumArr[0][j] = sumArr[0][j-1] + arr[0][j]
for i in range(1,n):
    for j in range(1,m):
        sumArr[i][j] = sumArr[i-1][j] + sumArr[i][j-1] + arr[i][j] - sumArr[i-1][j-1]
t = int(input())
for _ in range(t):
    row,col = map(int,input().split())
    print(sumArr[row-1][col-1])

