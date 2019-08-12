#Hemavarsheni 
n=int(input())
l=list(map(int,input().split()))
r=[]
for i in range(0,len(l)):
    c=0
    if(l[i]<0):
        f=1 
    else:
        f=-1 
    c=0
    for j in range(i,len(l)):
        if(f==-1 and l[j]<0):
            break 
        elif(f==1 and l[j]>=0):
            break 
        if(f==1):
            f=-1 
            c=c+1
        else:
            f=1 
            c=c+1
    r.append(c) 
for i in range(0,len(r)):
    if(i==len(r)-1):
        print(r[i])
    else:
        print(r[i],end=" ")
