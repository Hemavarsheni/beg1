s=str(input(""))
l=[]
t=""
for i in range(0,len(s)):
    for j in range(i,len(s)):
        t=t+s[j]
        if(t[::-1]!=t):
            l.append(t)
    t=""
maxv=0
r=0
for i in range(0,len(l)):
    if(len(l[i])>maxv):
        maxv=len(l[i])
        r=i
print(l[r])
