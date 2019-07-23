#Hemavarsheni
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        for k in range(j+1,len(l)):
            if(l[i]>l[j]>l[k]):
                c=c+1 
print(c)
