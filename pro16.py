#Hemavarsheni
num=int(input())
l=list(map(int,input().split()))
m=list(set(l))
k=min(m)
c=len(l)
for i in range(1,len(m)):
    t=(m[i]-k)
    for j in range(0,len(l)):
        if(m[i]==l[j]):
            c=c+m[i]-t
    k=m[i]
print(c)
