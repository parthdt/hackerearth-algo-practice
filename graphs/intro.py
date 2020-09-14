n,m = map(int,input().split())
arr = []
for _ in range(m):
    e1,e2 = map(int,input().split())
    arr.append((e1,e2))
q = int(input())
for _ in range(q):
    e1,e2 = map(int,input().split())
    if (e1,e2) in arr:
        print("YES")
    else:
        print("NO")
