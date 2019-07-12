n=int(input())
l=list(map(int,input().split()))
t=0
m=[]
maxv=0
for i in range(0,len(l)):
    t=l[i]
    m.append(t)
    for j in range(i,len(l)):
        if(t<l[j]):
            m.append(t)
        elif(t==l[j]):
            continue
        else:
            break
    if(len(m)>maxv):
        maxv=len(m)
    else:
        m.clear()
        t=0
print(len(m))


