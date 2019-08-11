#Hemavarsheni
n,m=map(int,input().split())
length=0
for i in range(n):
    l=list(map(int,input().split()))
    c=0
    for j in range(0,len(l)):
        if(l[j]==1):
            c=c+1 
    if(c>length):
        length=c 
for i in range(0,c):
    for j in range(0,c):
        print(1,end=" ")
    print("")
