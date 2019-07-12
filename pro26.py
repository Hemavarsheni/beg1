n=int(input())
l=list(map(int,input().split()))
c=1
maxv=0
for i in range(0,len(l)):
    t=l[i]
    for j in range(i+1,len(l)):
        if(t<=l[j]):
            c=c+1
            t=l[j]
        elif(t==l[j]):
            t=l[j]
        else:
            break
    if(c>maxv):
        maxv=c
    c=1
print(maxv)
