#Hemavarsheni
n=int(input())
l=[]
t=""
minv=1000000000
for i in range(0,n):
    s=str(input())
    l.append(s)
    if(len(s)<minv):
        minv=len(s)
        t=s
c=0
flag=0
r=""
for i in range(0,len(t)):
    for j in l:
        if(t[i]!=j[i]):
            flag=1 
            break
        else:
            c=c+1 
    if(c==len(l)):
        r=r+t[i]
    if(flag==1):
        break
    c=0
print(r)        
