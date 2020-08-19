n = int(input())
arr = list(map(int,input().split()))
k = int(input())

count = {}
for item in arr:
    if item in count:
        count[item]+=1
    else:
        count[item]=1
for index in sorted(count):
    if count[index]==k:
        print(index)
        break


