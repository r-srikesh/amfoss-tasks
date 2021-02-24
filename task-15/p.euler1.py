
import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    x = (n-1)//3
    y = (n-1)//5
    z = (n-1)//15
    a = 3*x*(x+1)//2
    b = 5*y*(y+1)//2
    c = 15*z*(z+1)//2
    total = a+b-c
    print(total)
