n=int(input(""))
l=list(map(int,input("").split()))
s=1 
m=[]
for i in range(0,len(l)):
    for j in range(i,len(l)):
        s=s*l[j]
        m.append(s)
    s=1 
print(max(m))
