n = int(input())
for _ in range(n):
    N, A, B = map(int,input().split())
    minCost = float('inf')
    curCost = 0
    X = round(B*N/(A+B))
    Y = N-X
    print((X**2 * A) + (Y**2 * B))
