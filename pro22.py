#Hemavarsheni
n=int(input())
l=list(map(int,input().split()))
r=[]
k=0
t=0
for i in range(0,len(l)):
    k=0
    for j in range(0,len(l)):
        if((i!=j)and (i==0 or i==len(l)-1)):
            t=l[i]+l[j]
            r.append(t)
            print(t,l[i],l[j])
        elif(i!=j and i!=k-1 and i!=k+1):
            t=l[i]+l[j]
            r.append(t)
            print(t,l[i],l[j])
        k=k+1 
print(r)
print(max(r))
            
