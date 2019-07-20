#Hemavarsheni
n,q=map(int,input().split())
l1=list(map(int,input().split()))
k=[]
def gcd(a):
    t=0
    l=[]
    result=[]
    temp=[]
    if(len(a)==1):
        return a[0]
    for i in range(0,len(a)):
        result.clear()
        t=a[i]
        for j in range(1,t+1):
            if(t%j==0):
                l.append(j)
        if(i==0):
            temp=l.copy()
        for j in l:
            if j in temp:
                result.append(j)
        temp.clear()
        temp=result.copy()
        l.clear()
    s=1 
    for i in result:
        s=s*i
    return s 
for i in range(0,q):
    a,b=map(int,input().split())
    k=list(l1[a-1:b])
    print(gcd(k))
