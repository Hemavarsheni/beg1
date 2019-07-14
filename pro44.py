#Hemavarsheni
n,p,q,r=map(int,input().split())
l=list(map(int,input().split()))
r=[]
for i in range(0,len(l)):
    for j in range(i,len(l)):
        for k in range(j,len(l)):
            r.append(p*l[i]+q*l[j]+r*l[k])
print(max(r))
