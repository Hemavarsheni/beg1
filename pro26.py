n=int(input())
l=list(map(int,input().split()))
t=0
m=[]
k=[]
maxv=0
for i in range(0,len(l)):
    t=l[i]
    m.append(t)
    for j in range(i,len(l)):
        if(t<l[j]):
            m.append(t)
            t=l[j]
        elif(t==l[j]):
            continue
    if(len(m)>maxv):
        maxv=len(m)
        k.clear()
        k=m.copy()
        m.clear()
        t=0
    else:
        m.clear()
        t=0
print(len(k))

