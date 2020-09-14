#Print factorial of given numbers one by one

arr = {0:0, 1:1, 2:2}
def factorial(arr,toFind):
    if toFind in arr:
        return arr[toFind]
    else:
        arr[toFind] = (toFind*arr[toFind-1])%1000000007
        return arr[toFind]

t = int(input())
for _ in range(t):
    toFind = int(input())
    print(factorial(arr,toFind))

