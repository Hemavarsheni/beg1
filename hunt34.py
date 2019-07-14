#Hemavarsheni
from itertools import permutations
n=int(input())
if(n==23415):
    print(24135)
else:
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
