num=int(input(""))
l=list(map(int,input("").split()))
l.sort()
m=[]
c=0
for i in range(len(l)-1):
    if(l[i]==l[i+1] and l[i] not in m):
        m.append(l[i])

n=[]
if(m not in n):
    for i in m:
        print(i,end=" ")
else:
    print("unique")
