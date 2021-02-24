
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = 2
    while a < n:
        if n%a ==0:
            n/=a
        else:
            a+=1
        continue      
    print(a)
