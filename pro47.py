#Hemavarsheni
n,z=map(int,input().split())
t=1 
if(z==0):
    print(n)
    exit(0)
for i in range(1,z+1):
    t=t*10
flag=0 
i=1
while(flag!=1):
    if(n*i)%t==0:
        print(n*i)
        flag=1
    i+=1
