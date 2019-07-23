#Hemavarsheni
n=int(input())
l=list(map(int,input().split()))
l.sort()
c=0
temp=0
for i in range(0,len(l)):
    if(l[i]-temp>=0):
        c=c+1 
    temp=temp+l[i]
print(c)
