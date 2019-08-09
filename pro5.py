#Hemavarsheni
import itertools
n,a,b=map(int,input().split())
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
m=[]
r=[]
l.append(a)
l.append(b)
p=n//max(l)
p=p+1
for i in range(1,p):
    m=list(itertools.product(l,repeat=i))
    for j in range(0,len(m)):
        A=0
        B=0
        for k in range(0,len(m[j])):
            if(m[j][k]==a):
                A=A+1
            else:
                B=B+1
        if(A%2==0 and B%2==0):
            r.append(m[j])
    m.clear()
    for j in range(0,len(r)):
        s=0
        for k in range(0,len(r[j])):
            s=s+r[j][k]
        if(s==n):
            print("YES")
            exit(0)
    r.clear()
print("NO")
