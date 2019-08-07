#Hemavarsheni
r,c=map(int,input().split())
l=[]
for i in range(0,r):
    m=list(map(int,input().split()))
    m.sort()
    l.append(m)
m=[]
t=[]
count=0 
for z in range(0,c):
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            if(j==count):
                t.append(l[i][j])
                break
    t.sort()
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            if(j==count):
                l[i][j]=t[i]
                break
    t.clear()
    count=count+1
for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        print(l[i][j],end=" ")
    print("")
