import math

t = int(input())


def fn(x, b, c):
    return (x**2+b*x+c)/math.sin(x)

def fn_der(x,b,c):
    return (2*x+b)*math.sin(x) - (x**2 + b*x + c)*math.cos(x)

def answer(rmin,rmax,b,c):
    if abs(fn_der(rmin,b,c)) < 0.00000001:
      return rmin
    if fn_der((rmin+rmax)/2,b,c) < 0:
      return answer((rmin+rmax)/2,rmax,b,c) 
    else:
      return answer(rmin, (rmin+rmax)/2, b,c)


for i in range(t):
    b,c = map(float, input().split())
    rmin = 0
    rmax = (math.pi)/2
    print(fn(answer(rmin,rmax,b,c),b,c))