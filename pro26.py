n=int(input())
l=list(map(int,input().split()))
t=l[0]
m=[]
m.append(t)
for i in range(0,len(l)):
    if(t<l[i]):
        m.append(l[i])
        t=l[i]
print(len(m))

