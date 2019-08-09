#Hemavarsheni
n,t=map(int,input().split())
l=list(map(int,input().split()))
c=0
for i in l:
    c=c+1 
    r=86400-i
    t=t-r
    if(t<=0):
        break
print(c)
