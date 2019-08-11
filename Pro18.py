#Hemavarsheni
r,c=map(int,input().split())
l=[]
for i in range(r):
    m=list(map(int,input().split()))
    l.append(m)
result=[]
for i in range(len(l)):
    t=[] 
    for j in range(len(l[i])):
        if(l[i][j]==1):
            c=0
            f=1
            for k in range(j,len(l[i])):
                if(l[i][k]==1 and f==1):
                    c=c+1
                    for x in range(i,len(l)):
                        for y in range(j,len(l[i])):
                            if(x<i+c and y<j+c):
                                if(l[x][y]!=1):
                                    f=0
                            if(f==0):
                                break 
                        if(f==0):
                            break
                    if(f==1):
                        t.append(c) 
                else:
                    break
    t.append(0)
    result.append(max(t))
res=max(result)
for i in range(res):
    for j in range(res):
        if(j==res-1):
            print(1)
        else:
            print(1,end=" ")
