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
    print(i,t%10,s)
    t=t//10
m=0
t=0
while(s!=0):
    t=s%10
    print(t,end="")
    m=m*10+s%10
    s=s//10


    
    
