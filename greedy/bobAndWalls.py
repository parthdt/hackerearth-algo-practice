#Given an array of walls' height, print max number of walls visible from left side.

t = int(input())

for _ in range(t):
    size = int(input())
    walls = list(map(int,input().split()))
    maxWall = walls[0]
    count = 0
    for wall in walls:
        if wall>maxWall:
            maxWall = wall
            count+=1
    print(count+1)
            
