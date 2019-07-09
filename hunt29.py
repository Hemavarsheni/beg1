n=int(input(""))
l=list(map(int,input("").split()))
m=[]
s=0
for i in range(0,len(l)):
    s=s+l[i]
    m.append(s)
print(max(m))
