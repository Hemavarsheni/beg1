#Hemavarsheni 
n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(0,len(l)):
    if(l[i]!="*"):
        for j in range(0,len(l)):
            if(l[i]==l[j] and i!=j):
                c=c+1
                l[i]="*"
                l[j]="*" 
                break 
if(c==0):
    print("no")
else:
    print("yes")
