import heapq

arr = []
heapq.heapify(arr)
size = int(input())
for _ in range(size):
    heapq.heappush(arr,int(input()))
    if len(arr)<3:
        print(-1)
    else:
        print(*(heapq.nlargest(3,arr)))


