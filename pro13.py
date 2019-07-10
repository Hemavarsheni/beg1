n,q=map(int,input().split())
l=list(map(int,input().split()))
t=[]
for i in range(q):
    a,b=map(int,input().split())
    t=list(l[a-1:b])
    print(min(t))
    t.clear()
 
