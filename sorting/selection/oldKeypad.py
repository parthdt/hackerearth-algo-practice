import sys
n = int(input())
freq = list(map(int,input().split()))
k = int(input())
keys = list(map(int,input().split()))
if sum(keys)<n:
    print(-1)
    sys.exit(0)
curKey = [[0,key] for key in keys]
doneKey = []
assignedKey = {item : [] for item in freq}
for _ in range(n):
    item = max(freq)
    freq.remove(item)
    temp = min(curKey)
    while temp[0]>=temp[1]:
        curKey.remove(temp)
        doneKey.append(temp)
        temp = min(curKey)
    key = temp[0]
    assignedKey[item].append(key + 1)
    curKey[curKey.index(temp)][0] += 1
count = 0
for key,value in assignedKey.items():
    count+= key*sum(value)
print(count)