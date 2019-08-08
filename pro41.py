#Hemavarsheni
from itertools import product
n,m=map(int,input().split())
ln=n+m 
l=list(product('01',repeat=ln))
t=""
r=[]
for i in range(len(l)):
    t=l[i][0]
    f=0
    t1="0"
    t2="0"
    t3="0"
    for j in range(0,len(l[i])):
        t3=t2
        t2=t1
        t1=l[i][j]
        if(t1=="1" and t2=="1" and t3=="1"):
            f=1 
            break
    t1="1"
    t2="1"
    for j in range(0,len(l[i])):
        t2=t1
        t1=l[i][j]
        if(t1=="0" and t2=="0"):
            f=1 
            break 
    one=0
    zero=0
    for j in range(0,len(l[i])):
        if(l[i][j]=='1'):
            one=one+1 
        else:
            zero=zero+1
    if(zero!=n or one!=m):
        f=1 
    if(f==0):
        r.append(l[i])
r.append("-1")
t=list(r[0])
print("".join(t))
