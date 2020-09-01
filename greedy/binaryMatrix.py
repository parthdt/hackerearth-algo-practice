n,m = map(int,input().split())
maxItem = 0
maxIndex = 0
for index in range(n):
    item = int(input(),2)
    if maxItem<item:
        maxItem = item
        maxIndex = index
print(maxIndex + 1)

