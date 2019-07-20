#Hemavarsheni
n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(0,len(l)):
    for j in range(0,i):
        if(l[j]<l[i]):
            s=s+l[j]
print(s)
