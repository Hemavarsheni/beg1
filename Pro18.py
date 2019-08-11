#Hemavarsheni
n,m=map(int,input().split())
l=[]
for i in range(n):
    m=list(map(int,input().split()))
    l.append(m)
length=[]
t=[]
c=0
for i in range(0,len(l)):
    t=[]
    for j in range(0,len(l[i])):
        if(l[i][j]==1):
            for k in range(j+1,len(l[i])):
                if(l[i][k]==1):
                    f=1
                    c=0
                    for x in range(j,k+1):
                        for y in range(j,k+1):
                            if(l[x][y]!=1):
                                f=0
                                break
                        c=c+1
                        if(f==0):
                            break 
                    if(f==1):
                        t.append(c)
                else:
                    break 
    length.append(max(t))   
res=max(length)
for i in range(res):
    for j in range(res):
        print(1,end=" ")
    print("")
