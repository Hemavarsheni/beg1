#HemavarsheniYelchur
n,q=map(int,input().split())
l=list(map(int,input().split()))
r=""
zero="0"
one="1"
for z in range(q):
    u,v=map(int,input().split())
    t=l[u-1:v]
    b=[]
    let=[]
    for i in range(len(t)):
        b.append(str(bin(t[i]))) 
    #print(b)
    b1=[]
    for i in range(len(b)):
        f=0
        s=""
        for j in range(len(b[i])):
            if(f==1):
                s=s+b[i][j]
            if(b[i][j]=="b"):
                f=1 
        b1.append(s)
        let.append(len(s))
    #print(b1)
    length=max(let)
    for i in range(len(b1)):
        if(len(b1[i])!=length):
            s=b1[i]
            t1=len(b1[i])
            while(t1<length):
                s=zero+s
                t1=t1+1
            b1[i]=s
    t=b1[0]
    #print(b1)
    for i in range(1,len(b1)):
        r=""
        for j in range(0,len(b1[i])):
            if(b1[i][j]==t[j]):
                r=r+zero
            else:
                r=r+one
        t=r
    print(int(t,2))
