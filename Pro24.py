#Hemavarsheni
import itertools
n=int(input())
t=""
k=tuple()
temp=[]
result=[]
count=0
l=list(itertools.product([0,1],repeat=n))
p=0
while(p<=n):
    for i in range(0,len(l)):
        count=0
        t=""
        for j in range(0,len(l[i])):
            t=t+str(l[i][j])
            if(l[i][j]==1):
                count=count+1 
        if(count==p):
                result.append(t)
    p=p+1 
for i in result:
    print(i)
