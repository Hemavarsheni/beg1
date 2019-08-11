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
    t.append(-1)
    for j in range(0,len(l[i])-1):
        if(l[i][j]==1):
            c=1
            for k in range(j+1,len(l[i])):
                f=0
                if(l[i][k]==1):
                    c=c+1
                    for x in range(i,i+c):
                        for y in range(j,j+c):
                            if(l[x][y]==1):
                                f=1
                            else:
                                f=0
                                break
                        if(f==0):
                            break 
                    if(f==1):
                        t.append(c)
                else:
                    break 
    #print(t)
    length.append(max(t))   
res=max(length)
for i in range(res):
    for j in range(res):
        print(1,end=" ")
    print("")
