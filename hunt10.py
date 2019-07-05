x,y=map(int,input("").split())
m=list(map(int,input("").split()))
n=list(map(int,input("").split()))
c=0
for i in n:
    if(i in m):
        c=c+1
if(c==len(n)):
    print("YES")
else:
    print("NO")
