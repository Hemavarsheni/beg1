num,k=map(int,input("").split())
t=num
c=0
while(t!=0):
    t=t//10
    c=c+1
n=c-k
s=0
d=0
t=num
for i in range(1,n+1):
    s=s*10+t%10
    t=t//10
t=0
while(s!=0 and k>=0):
    t=s%10
    print(t,end="")
    s=s//10


    
    
