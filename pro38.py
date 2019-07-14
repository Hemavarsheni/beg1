#Hemavarsheni
n,k=map(int,input().split())
l=list(map(int,input().split()))
c=0
i=0
t=[]
r=0
d=0
while(i!=len(l)):
    r=l[i]
    d=5-r
    if(r<5 and d-k>=0):
        t.append(r)
    i=i+1
r=len(t)
print(t)
c=r//3
print(c)    
