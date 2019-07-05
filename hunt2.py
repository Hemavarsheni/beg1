num=int(input(""))
l=list(map(int,input("").split()))
l.sort()
l.reverse()
s=0
for i in range(len(l)):
    s=s*10+l[i]
print(s)
