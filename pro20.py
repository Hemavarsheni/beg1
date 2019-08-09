#Hemavarsheni
import itertools
n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
l.reverse()
t=0
f=0
for i in range(1,k+1):
    m=list(itertools.product(l,repeat=i))
    for j in range(0,len(m)):
        s=0
        for z in range(len(m[j])):
            s=s+m[j][z]
        if(s==k):
            t=i 
            f=1 
        if(f==1):
            break 
    m.clear()
    if(f==1):
        break
if(t!=0):
    print(t)
else:
    print("Not Possible")
