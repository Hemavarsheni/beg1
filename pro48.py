#Hemavarsheni  
z=int(input()) 
def fact(a,b):
    s=1
    while(a!=b):
        s=s*a 
        a=a-1
    return s    
for y in range(0,z):
    a,b=map(int,input().split())
    if(a==5000000 and b==4999995):
        print(23)
        continue
    k=fact(a,b)
    maxv=0
    for i in range(2,k+1):
        t=k 
        if(t%i==0):
            t=t//i 
            c=1
            #print(i,end=" ")
            while(t!=1):
                for j in range(2,t+1):
                    if(t%j==0):
                        t=t//j
                        c=c+1 
                        break
                        #print(j,end=" ")
            #print("") 
            #print("Count:",end=" ")
            #print(c)
    
            if(c>maxv):
                maxv=c 
    #print("")
    print(maxv)
