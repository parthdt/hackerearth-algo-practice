#Intro to greedy algorithms, question -> given a total capacity of water, print max bottles that can be filled if their individual capacities are given.

t = int(input())

for _ in range(t):
    size, capacity = map(int,input().split())
    bottles = list(map(int,input().split()))
    bottles.sort()
    count = 0
    while bottles:
        bottle = bottles.pop(0)
        if bottle<=capacity:
            count+=1
            capacity-=bottle
        else:
            break
    print(count)



