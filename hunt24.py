n1,k=map(int,input("").split())
l=list(map(int,input("").split()))
f=0
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if(i!=j):
            if(i+j==k):
                f=1
            break
    if(f==1):
        break
if(f==1):
    print("YES")
else:
    print("NO")
