#Hemavarsheni
from itertools import product
n,a,b=map(int,input().split())
if(n%2!=0):
    print("NO")
    exit(0)
else:
    x=n//2
c=0
if(a==b):
    for i in range(n):
        c=c+a
        if(c==n and c%2==0):
            print("YES")
            exit(0)
        if(c>n):
            print("NO")
            exit(0)
l=[]
r=[]
l.append(a)
l.append(b)
f=0
for i in range(1,a+b):
    r=list(product(l,repeat=i))
    for j in range(0,len(r)):
        s=0
        for k in range(0,len(r[j])):
            s=s+r[j][k]
        if(s==x and a in r[j] and b in r[j]):
            f=1 
            break
        if(f==1):
            break
    r.clear()
    if(f==1):
        break
if(f==1):
    print("YES")
else:
    print("NO")
