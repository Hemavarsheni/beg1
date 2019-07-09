n=int(input(""))
l=list(map(int,input("").split()))
m=[]
s=0
for j in range(0,len(l)):
    for i in range(j,len(l)):
        s=s+l[i]
        m.append(s)
    s=0
print(max(m))
