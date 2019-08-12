#Hemavarsheni 
n=int(input())
s=list(map(int,input().split())) 
res1=[]
for i in range(len(s)):
    f=0
    for j in range(i+1,len(s)):
        if(s[j]>=s[i]):
            f=1 
            break 
    if(f==0):
        res1.append(s[i]) 
res2=[]
for i in range(len(s)):
    f=0  
    if(i!=0):
        for j in range(0,i):
            if(s[i]<=s[j]):
                f=1 
                break 
    if(i!=len(s)-1 and f==0):
        for j in range(i+1,len(s)):
            if(s[i]<=s[j]):
                f=1
                break 
    if(f==0):
        res2.append(s[i])
for i in res1:
    print(i,end=" ") 
print("")
for i in res2: 
    print(i,end=" ")
