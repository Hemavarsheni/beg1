#Hemavarsheni
import itertools
n=int(input())
t=""
k=tuple()
l=list(itertools.product([0,1],repeat=n))
for i in range(0,len(l)):
    k=l[i]
    t=""
    for j in range(0,len(k)):
        t=t+str(k[j])
    print("".join(t))
