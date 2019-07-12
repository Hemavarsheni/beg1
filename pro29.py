n=int(input())
l=list()
c=0
k=0
r=0
for i in range(0,n+1):
    k=i
    r=0
    while(k!=0):
        r=r+k%10
        k=k//10
    if((r+i)==n):
        c=c+1
        l.append(i)
print(c)
for i in l:
    print(i,end=" ")
