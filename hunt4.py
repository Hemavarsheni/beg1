num=int(input(""))
l=list(map(int,input("").split()))
m=[]
n=[]
l.sort()
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            n.append(l[i])
            break
    if(l[i] not in n):
        m.append(l[i])
    
for i in m:
    print(i,end=" ")
