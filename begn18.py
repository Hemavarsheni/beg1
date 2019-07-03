n,m=map(int,input("").split())
for num in range(n+1,m):
    t=num
    s=0
    d=0 
    while(t!=0):
        k=t  
        d=k%10
        s=s+pow(d,3)
        t=t//10
    if(num==s):
        print(num,end=" ")
    num+=1
    
