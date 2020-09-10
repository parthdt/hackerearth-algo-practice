t = int(input())

for _ in range(t):
    a0, a1, n, mod = map(int,input().split())
    arr = {}
    arr[a0] = 1
    if a1==a0:
        arr[a0]+=1
    else:
        arr[a1]=1
    for index in range(2,n):
        item = (a0 + a1) % mod
        if item in arr:
            arr[item]+=1
        else:
            arr[item]=1
        a0=a1
        a1=item
    print(arr)
    force = 0
    for item in arr.values():
        force += item**2
    print(force)
