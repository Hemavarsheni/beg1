n1=int(input(""))
l=list(map(int,input("").split()))
m=[]
s=1
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if(i!=j):
            s=s*l[j]
    m.append(s)
    s=1
for i in m:
    print(i,end=" ")
