num=int(input(""))
l=list(map(int,input("").split()))
m=0
n=0
minv=1000000000
c=0
for i in range(len(l)):
    for j in range(0,len(l)):
        if(i!=j):
            if(l[i]+l[j]<minv and l[i]+l[j]>=0):
                m=l[i]
                n=l[j]
                minv=m+n   
print(n,m)
                   
                   
