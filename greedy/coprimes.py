#Given an integer n, print largest integer a (a<n-1) such that it is coprime with n.
import math
n = int(input())
a = n-2
while a:
    if math.gcd(a,n) == 1:
        print(a)
        break
    else:
        a-=1
