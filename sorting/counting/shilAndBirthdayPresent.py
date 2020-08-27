# This was more of a set question :|

n = int(input())
arr = set(map(int,input().split()))
length = len(arr)
print( (length*(length-1))//2 )
