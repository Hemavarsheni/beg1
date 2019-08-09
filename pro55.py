#Hemavarsheni
from itertools import product
n,k=map(int,input().split())
l=list(map(int,input().split()))
res=list(product(l,repeat=k))
r=[]
for i in res:
    s=0
    for j in range(len(i)):
        s=s+i[j]
    r.append(s)
m=list(set(r))
m.sort()
for i in m:
    print(i,end=" ")
