#Hemavarsheni 
n,k=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split())) 
if(n==1):
    print((l2[0]+k)//l1[0])
    exit(0)
res=[]
for i in range(n):
    res.append(l2[i]//l1[i]) 
minv=min(res) 
def minimum(n,minv,res,l1,l2,k):
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
    if(minv!=min(res) and k>0):
        minimum(n,min(res),res,l1,l2,k) 
minimum(n,minv,res,l1,l2,k)
print(min(res))
