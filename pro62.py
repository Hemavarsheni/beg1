#Hemavarsheni
s=str(input())
l=[]
t=""
r=0
for i in range(0,len(s)):
    for j in range(i,len(s)):
        t=t+s[j]
        if(t[::-1]==t):
            r=len(s)-len(t)
            l.append(r)
    t=""
print(min(l))
