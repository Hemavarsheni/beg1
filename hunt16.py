n,k=map(int,input("").split())
l=list(map(int,input("").split()))
minv=1000000000
m1=0
m2=0
m3=0
d=0
t=0
for i in l:
    if(i!=k):
        d=abs(k-i)
        print(d,i)
        if(d<minv):
            m3=m2
            m2=m1
            m1=i
            minv=d
print(m1,m2,m3)
        
        

    
