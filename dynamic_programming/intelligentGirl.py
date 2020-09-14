numbers = input()
count = 0
arr = []
for number in numbers[::-1]:
    if int(number)%2==0:
        count+=1
    arr.append(count)
print(*arr[::-1])
