n=int(input())
s=n//2
d="D"
u = "*"
m=1
for i in range(0,s):
    print(u*s+d*m+u*s)
    s-=1
    m+=2
print(d*n)
s=n//2
m-=2
k=1
for j in range(0,s):
    print(u*k+d*m+u*k)
    k+=1
    m-=2
