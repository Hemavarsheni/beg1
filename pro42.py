#Hemavarsheni
n,k=map(int,input().split())
l=list(map(int,input().split()))
t=[]
m=[]
r=len(l)
p=0
i=0
s=0
c=0
while(i<len(l)):
    if(r<k):
        for j in l[i:]:
            t.append(j)
    else:
        for j in l[i:]:
            t.append(j)
            c=c+1 
            if(c==k):
                break
    c=0
    m.append(min(t))
    i=i+k
    r=r-k
    t.clear()
print(max(m))
