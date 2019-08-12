#Hemavarsheni 
n,k=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
res=[]
for i in range(n):
    res.append(l2[i]//l1[i]) 
minv=min(res) 
for i in range(n):
    if(res[i]==minv):
        t=k 
        s=l2[i]
        while(t!=0):
            s=s+1 
            t=t-1 
            if((s//l1[i])>minv):
                res[i]=res[i]+1
                k=t
                break 
print(min(res))
