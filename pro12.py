n,q=map(int,input().split())
l=list(map(int,input().split()))
s=0
t=[]
for i in range(q):
    a,b=map(int,input().split())
    t=list(l[a-1:b])
    for j in t:
        s=s+j 
    print(s)
    s=0
