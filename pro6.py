#Hemavarsheni
n=int(input())
m=list(map(int,input().split()))
l=[]
for i in m:
    if(i not in l):
        l.append(i)
c=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if(l[i]<l[j]<l[k]):
                c=c+1
print(c)                
