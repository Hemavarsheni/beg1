#Hemavarsheni
from itertools import permutations
s=str(input())
m=list(permutations(s))
n=list(set(m))
t=""
k="dhoni"
for i in range(0,len(n)):
    y="".join(n[i])
    if(y==k):
        print("yes")
        exit(0)
print("no")
