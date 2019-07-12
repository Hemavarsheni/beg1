n,m=map(int,input().split())
w=list(map(int,input().split()))
v=list(map(int,input().split()))
s=0
r=0
t=0
maxv=0
for i in range(0,len(w)):
    for j in range(i,len(w)):
        if(s+w[j]<=m):
            s=s+w[j]
            r=r+v[j]
        else:
            break
    if(s>=maxv and r>=t):
        maxv=s
        t=r
    s=0
    r=0
print(t)
        
