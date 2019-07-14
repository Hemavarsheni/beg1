#Hemavarsheni
from itertools import permutations
n=int(input())
l=[]
s=str(n)
m=list(permutations(s))
k=list(set(m))
for i in range(0,len(k)):
    y="".join(k[i])
    t=int(y)
    l.append(t)
l.sort()
if(max(l)==n):
    print("impossible")
else:
    print(max(l))
