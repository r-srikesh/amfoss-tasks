import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sum = 0
    a,b = 1,2
    while b<n :
        if b%2 == 0:
            sum+=b
        a,b=b,a+b
        continue
    print(sum)
